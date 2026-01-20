from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('student/', include('app_student_info.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)