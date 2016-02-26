from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='games'),
    url(r'^search/', views.search, name='games_search'),
    url(r'^box_score/(\d+)/', views.box_score, name='box_score'),
]

