from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from feedback.models import QRCode
from .models import UserEmployeur, Post
from .serializers import UserEmployeurSerializer, PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_emp.models import UserEmployeur

class UserEmployeurViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing UserEmployeur instances.
    """
    queryset = UserEmployeur.objects.all()
    serializer_class = UserEmployeurSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Post instances.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class GetQRCodeView(APIView):
    """
    Retrieve a QR code based on the user's email.
    """

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        if not email:
            return Response(
                {"error": "Email is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Get the user associated with the email
            user = UserEmployeur.objects.get(email=email)

            # Retrieve the QR code linked to the user
            qr_code = QRCode.objects.get(user=user)

            return Response(
                {"email": user.email, "qr_code": qr_code.code},
                status=status.HTTP_200_OK
            )
        except UserEmployeur.DoesNotExist:
            return Response(
                {"error": "User with this email does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        except QRCode.DoesNotExist:
            return Response(
                {"error": "QR code for this user does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        


def get_user_from_qr_code(request, code):
    """
    View to retrieve user information based on the QR code.
    """
    # Get the QRCode instance
    qr_instance = get_object_or_404(QRCode, code=code)
    
    # Retrieve the associated user
    user = qr_instance.user
    
    # Return user details as JSON response
    return JsonResponse({
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone_number": user.phone_number,
        "post": user.post.title if user.post else None
    })