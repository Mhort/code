from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    # Maps the category page urls (rango, django, other frameworks)
    url(r'^category/(?P<category_name_url>\w+)$', views.category, name='category'),)