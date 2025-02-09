from django.template import loader
from django.http import HttpResponse
from .form import ItemForm
from .models import Item
from django.shortcuts import render


def list_items(request):
    items = Item.objects.select_related('category').all().values(
        'id', 'name', 'description', 'price', 'quantity', 
        'image', 'purchase_date', 'category__name'
        )
    print(items)
    template = loader.get_template('item/item_list.html')
    context = {
        'items': items
    }
    return HttpResponse(template.render(context, request))


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user  # Set the user field
            item.save()
            return render(
                request, 'item/item_list.html', {
                    'form': form,
                    'message': ['Item added successfully'],
                }
            )
    else:
        form = ItemForm()
    context = {'form': form}
    return render(request, 'item/add_item.html', context)


def edit_item(request):
    template = loader.get_template('item/edit_item.html')
    context = {}
    return HttpResponse(template.render(context, request))
