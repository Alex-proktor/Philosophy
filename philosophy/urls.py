from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
]
