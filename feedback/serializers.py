from rest_framework import serializers
from .models import Alert, QRCode, QRCodeFeedback, FormFeedback, SocialMediaFeedback

class QRCodeFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCodeFeedback
        fields = ['id', 'user','qr_code', 'content', 'rating','sentiment', 'langue', 'created_at']
        read_only_fields = ['sentiment', 'langue']

class FormFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFeedback
        fields = ['id', 'user', 'title', 'content', 'service', 'other_service','sentiment', 'langue', 'created_at']
        read_only_fields = ['sentiment', 'langue']

class SocialMediaFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaFeedback
        fields = ['id', 'username', 'content', 'sentiment','langue', 'created_at']

class QRCodeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Optional: Customize the representation of the related User field.

    class Meta:
        model = QRCode
        fields = ['id', 'user', 'code', 'created_at']


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'feedback_type', 'feedback_id', 'message', 'created_at', 'is_traitement']