from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.splash_page, name=''),
    url(r'^welcome/', views.splash_page, name='')
]
