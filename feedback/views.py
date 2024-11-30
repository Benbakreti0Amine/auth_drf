from rest_framework import viewsets
from .models import QRCode, QRCodeFeedback, FormFeedback, SocialMediaFeedback
from .serializers import QRCodeFeedbackSerializer, FormFeedbackSerializer, QRCodeSerializer, SocialMediaFeedbackSerializer

import qrcode
from django.http import HttpResponse
from feedback.models import QRCode


class QRCodeFeedbackViewSet(viewsets.ModelViewSet):
    queryset = QRCodeFeedback.objects.all()
    serializer_class = QRCodeFeedbackSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        qr_code = self.request.query_params.get('qr_code')
        if qr_code:
            queryset = queryset.filter(qr_code__code=qr_code)
        return queryset

class FormFeedbackViewSet(viewsets.ModelViewSet):
    queryset = FormFeedback.objects.all()
    serializer_class = FormFeedbackSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        service = self.request.query_params.get('service')
        if service:
            queryset = queryset.filter(service=service)
        return queryset

class SocialMediaFeedbackViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaFeedback.objects.all()
    serializer_class = SocialMediaFeedbackSerializer


class QRCodeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing QRCode instances.
    """
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer


def generate_qr_code_image(request, code):
    try:
        # Get the QRCode instance
        qr_instance = QRCode.objects.get(code=code)
        
        # Generate QR code image
        qr = qrcode.make(qr_instance.code)
        
        # Create an HTTP response with the image
        response = HttpResponse(content_type="image/png")
        qr.save(response, "PNG")
        return response
    except QRCode.DoesNotExist:
        return HttpResponse("QR Code not found", status=404)
