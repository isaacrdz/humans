from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^persons/$', views.person_list, name= 'person_list' ),
]