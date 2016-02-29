from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='teams'),
    url(r'^(\d+)/schedules/', views.schedule, name='teams_schedule'),
]
