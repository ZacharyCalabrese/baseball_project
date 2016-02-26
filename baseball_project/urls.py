"""baseball_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from games import views

urlpatterns = [
    #url(r'^$', views.home_page, name='games'),
    url(r'^games/search/', views.search, name='games_search'),
    url(r'^games/homeruns/(\d+)/', views.home_runs, name='homeruns'),
    url(r'^games/', views.home_page, name='games'),
    url(r'^admin/', admin.site.urls),
]
