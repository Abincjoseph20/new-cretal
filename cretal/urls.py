from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("mainapp.urls")),
    path("cart/",include("carts.urls")),
    path("accounts/",include("accounts.urls")),
    path("orders/",include("orders.urls")),
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
