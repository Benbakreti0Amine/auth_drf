from django.db.models.signals import post_save
from feedback.models import QRCodeFeedback, Alert, FormFeedback

def create_qr_code_alert(sender, instance, created, **kwargs):
    if created and instance.sentiment == 'negative':
        negative_feedback_count = QRCodeFeedback.objects.filter(sentiment='negative').count()
        if negative_feedback_count >= 5:
            Alert.objects.create(
                feedback_type='QRCodeFeedback',
                feedback_id=instance.id,
                message=f"5 Negative QRCode Feedbacks received, including the latest one from user ID {instance.user.id}"
            )

def create_form_feedback_alert(sender, instance, created, **kwargs):
    if created and instance.sentiment == 'negative':
        negative_feedback_count = FormFeedback.objects.filter(sentiment='negative').count()
        
        if negative_feedback_count >= 5:
            Alert.objects.create(
                feedback_type='FormFeedback',
                feedback_id=instance.id,
                message=f"5 Negative Form Feedbacks received, including the latest one from user ID {instance.user.id}"
            )