from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('blog/', include('blog.urls')),
    path('event/', include('event.urls')),
    path('create_user/', views.register, name='apach_create'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='apach_login'),
    path('logut/', LogoutView.as_view(template_name='registration/logut.html'), name='apach_logout'),
    path('about/', views.about, name='about')

]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
