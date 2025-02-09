from django.template import loader
from django.http import HttpResponse
from category.models import Category


def display_insight(request):
    categories = Category.objects.all().values()
    template = loader.get_template('insight/databoard.html')
    context = {
        'categories': categories
    }
    return HttpResponse(template.render(context, request))
