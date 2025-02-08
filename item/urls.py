from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list_items, name='list_items'),
    path('add', views.add_item, name='add_item'),
    path('edit', views.edit_item, name='edit_item'),
]
