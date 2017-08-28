from django.conf.urls import url
from . import views

urlpatterns = [
    # /worker/
    url(r'^$', views.index, name='index'),

    # /worker/skill/
    url(r'^skill/$', views.skillList, name='skillList'),

    # /worker/skill/skill_name
    url(r'^skill/(?P<skill_name>[A-Za-z][\w|\W]+)/$', views.skillDetail, name='skillDetail'),

    # /worker/city/
    url(r'^city/$', views.cityList, name='cityList'),

    # /worker/city/city_name
    url(r'^city/(?P<city_name>[A-Za-z][\w|\W]+)/$', views.cityDetail, name='cityDetail'),
]
