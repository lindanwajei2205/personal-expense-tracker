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


def pie_chart(request):
    # categories = Category.objects.all().values()
    # template = loader.get_template('insight/pie_chart.html')
    # context = {
    #     'categories': categories
    # }
    # return HttpResponse(template.render(context, request))
    return HttpResponse('Pie chart')