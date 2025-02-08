"""
URL configuration for expensetracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from category import urls as category_urls
from item import urls as item_urls
from insight import urls as insight_urls
from django.shortcuts import render


def user_profile(request):
    return render(request, 'accounts/profile.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('accounts/profile/', user_profile, name='account_profile'),
    path('item/', include(item_urls)),
    path('insight/', include(insight_urls)),
    path('', include(category_urls)),
]
