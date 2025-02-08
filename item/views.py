from django.template import loader
from django.http import HttpResponse
from .form import ItemForm
from django.shortcuts import render


def list_items(request):
    template = loader.get_template('item/item_list.html')
    context = {}
    return HttpResponse(template.render(context, request))


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': form, 'success': True}
            return render(request, 'item/item_list.html', context)
    else:
        form = ItemForm()
    context = {'form': form}
    return render(request, 'item/add_item.html', context)


def edit_item(request):
    template = loader.get_template('item/edit_item.html')
    context = {}
    return HttpResponse(template.render(context, request))
