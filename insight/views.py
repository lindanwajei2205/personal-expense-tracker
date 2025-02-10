from django.template import loader
from django.http import HttpResponse
from category.models import Category
from django.shortcuts import get_object_or_404, redirect
from item.models import Item
from comment.form import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import matplotlib.pyplot as plt
import io
import base64
import matplotlib
matplotlib.use('Agg')


@login_required(login_url='/')
def display_insight(request):
    categories = Category.objects.all().values()
    template = loader.get_template('insight/databoard.html')
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))


def pie_chart(request, id):
    # Fetch items in the selected category, extracting name and price
    items = Item.objects.filter(category_id=id).values('name', 'price')
    names = [item['name'] for item in items]
    prices = [float(item['price']) for item in items]

    if not prices or sum(prices) == 0:
        return "empty"

    plt.figure(figsize=(6, 6))
    plt.pie(
        prices,
        labels=names,
        autopct=lambda p: f'{p:.1f}%' if p > 0 else '',
        startangle=90,
    )
    plt.title("Price Distribution Among Items", fontsize=12, weight='bold')
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png).decode('utf-8')

    return graphic


@login_required(login_url='/')
def chart(request, id):
    get_selected_category = get_object_or_404(Category, id=id)
    
    # add comment form from comment app, and save if valid.  
    if (request.method == 'POST'):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.category = get_selected_category
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect('category_chart', id=id)
    else:
        # pass the selected category to the form
        comment_form = CommentForm(initial={'category': get_selected_category})

    categories = Category.objects.all().values()
    # get all items in the selected category
    items_in_category = Item.objects.filter(category_id=id).values(
        'id', 'name', 'description', 'price', 'quantity', 
        'image', 'purchase_date', 'category__name'
        )
    total_price = items_in_category.aggregate(total_price=Sum('price'))

    context = {
        'categories': categories,
        'selected_category_id': get_selected_category.id,
        'items': items_in_category,
        'total_price': total_price['total_price'],
        'pie_chart': pie_chart(request, id),
        'comment_form': comment_form,
    }
    template = loader.get_template('insight/databoard.html')
    return HttpResponse(template.render(context, request))