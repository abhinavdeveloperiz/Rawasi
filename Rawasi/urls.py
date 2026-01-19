from django.contrib import admin
from django.urls import path
from app.views import home, about, courses, blog, gallery, ourstudents, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('blog/', blog, name='blog'),
    path('gallery/', gallery, name='gallery'),
    path('ourstudents/', ourstudents, name='ourstudents'),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
