from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from Avtoapi.views import UserViewSet, NewsViewSet, SaleViewSet, GetSaleView, GetUserView

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('sale', SaleViewSet)
router.register('user', UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/user-filter/', GetUserView.as_view()),
    path('api/sale-filter/', GetSaleView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
