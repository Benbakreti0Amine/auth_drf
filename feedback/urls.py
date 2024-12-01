from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AllFeedbackStats,
    QRCodeFeedbackViewSet, 
    FormFeedbackViewSet, 
    SocialMediaFeedbackViewSet, 
    QRCodeViewSet, 
    generate_qr_code_image, 
    QRCodeFeedbackStats, 
    FormFeedbackStats, 
    SocialMediaFeedbackStats
)

# Initialisation du routeur pour les ViewSets
router = DefaultRouter()
router.register(r'qr-feedback', QRCodeFeedbackViewSet)
router.register(r'form-feedback', FormFeedbackViewSet)
router.register(r'social-feedback', SocialMediaFeedbackViewSet, basename='social-feedback')
router.register(r'qrcodes', QRCodeViewSet, basename='qrcode')

# Définir les chemins supplémentaires pour les vues statistiques
urlpatterns = [
    path('', include(router.urls)),  # Inclut les routes générées par le routeur
    path('generate-qr/<str:code>/', generate_qr_code_image, name='generate_qr'),  # Route pour générer un QR code
    path('api/qr-feedback/stats/', QRCodeFeedbackStats.as_view(), name='qr_feedback_stats'),  # Statistiques QR Feedback
    path('api/form-feedback/stats/', FormFeedbackStats.as_view(), name='form_feedback_stats'),  # Statistiques Form Feedback
    path('api/social-feedback/stats/', SocialMediaFeedbackStats.as_view(), name='social_feedback_stats'),  # Statistiques Social Feedback
    path('api/ALL/stats/', AllFeedbackStats.as_view(), name='all_feedback_stats'),  # Nouvelle route pour toutes les statistiques
]
