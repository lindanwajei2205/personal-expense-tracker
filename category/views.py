from django.http import HttpResponse
from django.template import loader
from .models import Category

# Create your views here.


def categories(request):
    categories = Category.objects.all().values()
    template = loader.get_template('category/categories.html')
    context = {
        'categories': categories
    }
    return HttpResponse(template.render(context, request))
