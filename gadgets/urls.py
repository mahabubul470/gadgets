from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.views import View


class RedirectProductView(View):

    def get(self, request):
        return redirect('products/list')


urlpatterns = [
    path("", RedirectProductView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('products/', include('product.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
