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
    path('accounts/', include('account.urls')),
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
    path('qc-nealit/', include('quality_control_nealit.urls')),
    path('qc-retest/', include('qc_retest.urls')),
    path('qc-block/', include('qc_block.urls')),
    path('', include('product_report.urls')),
    path('slider/', include('slider.urls')),
    path('qc-block-stucco/', include('qc_block_stucco.urls')),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
