from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('addpage', views.addpage, name='addpage'),
  path('add', views.add, name = 'add'),
  path('<int:contact_id>/view', views.view, name='view'),
  path('<int:contact_id>/delete', views.delete, name = 'delete'),
  path('<int:contact_id>/edit', views.edit, name='edit')

]
