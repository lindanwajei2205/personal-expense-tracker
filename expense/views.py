from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def expense_categories(request):
    return HttpResponse('Expense Categories')
