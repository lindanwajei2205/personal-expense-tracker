from django.template import loader
from django.http import HttpResponse
from .form import ItemForm
from .models import Item
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def list_items(request):
    items = Item.objects.select_related('category').all().values(
        'id', 'name', 'description', 'price', 'quantity', 
        'image', 'purchase_date', 'category__name'
        )
    template = loader.get_template('item/item_list.html')
    context = {
        'items': items
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/')
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user  # Set the user field
            item.save()
            messages.success(request, 'Item added successfully')
            return redirect('list_items')
    else:
        form = ItemForm()
    context = {'form': form}
    return render(request, 'item/add_item.html', context)


@login_required(login_url='/')
def edit_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully')
            return redirect('list_items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item/add_item.html', {'form': form})


@login_required(login_url='/')
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    messages.success(request, 'Item deleted successfully')
    return redirect('list_items')