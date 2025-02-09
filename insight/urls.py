from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_insight, name='display_insight'),
    # pie chart
    path('pie-chart/', views.pie_chart, name='pie_chart'),
]
