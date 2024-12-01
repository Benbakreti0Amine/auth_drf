from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QRCodeFeedbackViewSet, FormFeedbackViewSet, QRCodeViewSet, SocialMediaFeedbackViewSet, generate_qr_code_image

router = DefaultRouter()
router.register(r'qr-feedback', QRCodeFeedbackViewSet)
router.register(r'form-feedback', FormFeedbackViewSet)
router.register(r'social-feedback', SocialMediaFeedbackViewSet, basename='social-feedback')
router.register(r'qrcodes', QRCodeViewSet, basename='qrcode')
urlpatterns = [
    path('', include(router.urls)),
    path('generate-qr/<str:code>/', generate_qr_code_image, name='generate_qr'),    
]

