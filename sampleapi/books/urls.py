from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all/$', views.books, name="books"),
    url(r'^authors/$', views.authors, name="authors"),
]