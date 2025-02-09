from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_insight, name='display_insight'),
    path('category_chart/<int:id>/', views.chart, name='category_chart'),
]
