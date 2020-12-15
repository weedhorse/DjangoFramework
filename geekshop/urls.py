from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views as mainapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_views.index, name='index'),
    path('products/', mainapp_views.products, name='products'),
    path('test-context/', mainapp_views.test_context),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


