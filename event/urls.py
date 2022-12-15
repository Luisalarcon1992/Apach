from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='event'),
    path('create/', views.create, name='event_create'),
    path('view/<int:id>', views.view, name='event_view'),
    path('delete/<int:id>', views.delete, name='event_delete'),
    path('edit/<int:id>', views.edit, name='event_edit')
]