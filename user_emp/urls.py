from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GetQRCodeView, UserEmployeurViewSet, PostViewSet

router = DefaultRouter()
router.register(r'user-employeurs', UserEmployeurViewSet, basename='useremployeur')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('getqrcode/', GetQRCodeView.as_view(), name='get_qr_code'),
]
