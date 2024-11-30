import uuid
from django.db import models
from feedback.models import QRCode

class UserEmployeur(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, blank=True)

    def generate_qr_code(self):
        unique_code = str(uuid.uuid4())
        
        return QRCode.objects.create(
            user=self,
            code=unique_code
        )

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        
        super().save(*args, **kwargs)      
        if is_new:
            self.generate_qr_code()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.title