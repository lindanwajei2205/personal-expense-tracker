from django.template import loader
from django.http import HttpResponse


def display_insight(request):
    template = loader.get_template('insight/databoard.html')
    context = {}
    return HttpResponse(template.render(context, request))
