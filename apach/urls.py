from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('blog/', include('blog.urls')),
    path('event/', include('event.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
