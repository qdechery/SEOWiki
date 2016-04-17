from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^profile/$', views.profile, name='profile'),
    # url(r')
]