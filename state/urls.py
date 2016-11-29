from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^state/', views.state_list, name= 'state_list' ),
]