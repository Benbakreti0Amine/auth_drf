from django.apps import AppConfig
from django.db.models.signals import post_save

class FeedbackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feedback'

    def ready(self):
        from feedback.models import QRCodeFeedback, FormFeedback  # Import model here
        from feedback.signals import create_qr_code_alert, create_form_feedback_alert # Import signal handler

        # Connect the signal
        post_save.connect(create_qr_code_alert, sender=QRCodeFeedback)
        post_save.connect(create_form_feedback_alert, sender=FormFeedback)