from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.create_users, name='login'),
    path('blog/', include('blog.urls')),
    path('event/', include('event.urls')),
]
