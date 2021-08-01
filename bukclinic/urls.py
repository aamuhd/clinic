"""bukclinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('stock/', include(('stock.urls', 'stock'), namespace='stock')),
    path('generate_report/', include(('generate_report.urls', 'generate_report'), namespace='generate_report')),
    path('patientsrecords/', include(('patientsrecords.urls', 'patientsrecords'), namespace='patientsrecords')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = 'Clinic Management System'
admin.site.index_title = 'Clinic Admin Interface'
admin.site.site_title = 'My Clinic'
