from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('view/<int:id>', views.view, name='blog_view'),
    path('edit/<int:id>', views.edit, name='blog_edit'),
    path('create/', views.create, name='blog_create'),
    path('delete/<int:id>', views.delete, name='blog_delete'),
    #path('comment/<int:id>', views.comment, name='blog_comment')
]