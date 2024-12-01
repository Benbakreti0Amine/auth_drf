from django.db import models
from django.conf import settings
from users.models import User

class QRCode(models.Model):
    user = models.OneToOneField('user_emp.UserEmployeur', on_delete=models.CASCADE, related_name='qrcode')
    code = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"QR Code for {self.user.email}"

class QRCodeFeedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='qr_feedbacks')
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name='feedbacks')
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    sentiment = models.CharField(max_length=20, choices=[('positive', 'Positive'), ('neutral', 'Neutral'), ('negative', 'Negative') ] ,default='Neutral')
    langue = models.CharField(max_length=50,default='unknown')

    def __str__(self):
        return f"QR Feedback from {self.user.get_full_name()} for {self.user_employer.user.get_full_name()}"

class FormFeedback(models.Model):
    SERVICE_CHOICES = [
        ('ccp', 'CCP'),
        ('baridi_mob', 'Baridi Mob App'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='form_feedbacks')
    title = models.CharField(max_length=200)
    content = models.TextField()
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    other_service = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sentiment = models.CharField(max_length=20, choices=[('positive', 'Positive'), ('neutral', 'Neutral'), ('negative', 'Negative') ] ,default='Neutral')
    langue = models.CharField(max_length=50,default='unknown')

    def __str__(self):
        return f"Form Feedback: {self.title} by {self.user.get_full_name()} for {self.get_service_display()}"

class SocialMediaFeedback(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    sentiment = models.CharField(max_length=20, choices=[('positive', 'Positive'), ('neutral', 'Neutral'), ('negative', 'Negative') ] ,default='Neutral')
    langue = models.CharField(max_length=50,default='unknown')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Social Media Feedback from {self.username} on {self.platform}"

