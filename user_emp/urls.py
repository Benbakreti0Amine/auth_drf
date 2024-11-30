from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GetQRCodeView, UserEmployeurViewSet, PostViewSet, get_user_from_qr_code

router = DefaultRouter()
router.register(r'user-employeurs', UserEmployeurViewSet, basename='useremployeur')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('getqrcode/', GetQRCodeView.as_view(), name='get_qr_code'),
    path('get-user/<str:code>/', get_user_from_qr_code, name='get_user_from_qr_code'),
]
