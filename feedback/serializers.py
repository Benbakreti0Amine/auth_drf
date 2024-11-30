from rest_framework import serializers
from .models import QRCode, QRCodeFeedback, FormFeedback, SocialMediaFeedback

class QRCodeFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCodeFeedback
        fields = ['id', 'user','qr_code', 'content', 'rating', 'created_at']

class FormFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFeedback
        fields = ['id', 'user', 'title', 'content', 'service', 'other_service', 'created_at']

class SocialMediaFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaFeedback
        fields = ['id', 'username', 'platform', 'content', 'sentiment', 'created_at']

class QRCodeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Optional: Customize the representation of the related User field.

    class Meta:
        model = QRCode
        fields = ['id', 'user', 'code', 'created_at']