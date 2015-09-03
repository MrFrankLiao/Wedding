from django.conf.urls import include, url
from django.contrib import admin

from member import views
urlpatterns = [
    url(r'^$', views.LoginView, name='login_index'),
]
