"""IGPortal URL Configuration

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
from django.contrib.auth import views
from django.urls import path, include
from .views import home_page, about_page, header, footer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about-us', about_page),
    path('header', header, name="header"),
    path('footer', footer, name="footer"),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('account.urls')),
    path('bascule/', include('bascule.urls')),
    path('block/', include('block.urls')),
    path('canteen/', include('canteen.urls')),
    path('guard/', include('guard.urls')),
    path('hr/', include('hr.urls')),
    path('hse/', include('hse.urls')),
    path('image_processing', include('image_processing.urls')),
    path('iso/', include('iso.urls')),
    path('lab/', include('lab.urls')),
    path('ml/', include('ml.urls')),
    path('nealit/', include('nealit.urls')),
    path('plc/', include('plc.urls')),
    path('pm/', include('pm.urls')),
    path('product/', include('product.urls')),
    path('slider/', include('slider.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
