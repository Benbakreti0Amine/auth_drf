from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User
from django.contrib.auth.models import Permission
from .models import User, UserEmployer, Post, QRCode

class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ['id', 'username','password', 'email', 'first_name', 'last_name', 'is_active','password']#,'image','token'


    def validate(self, attrs):
     email = attrs.get("email")  # Use get() method to safely retrieve email field

     if email:
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError("Email has already been used")

     return super().validate(attrs)


    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()


        return user


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)




class ResetPasswordSerializer(serializers.Serializer):
    """
    Reset Password Serializer.
    """

    new_password = serializers.CharField(write_only=True,min_length=1)

    class Meta:
        field = ("new_password")

    def validate(self, data):
        """
        Verify token and encoded_pk and then set new password.
        """
        password = data.get("new_password")
        print(password)
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        print(pk)
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")
        print(user)
        user.set_password(password)
        user.save()
        return data

class NewPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)



# serializers for user emp
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name', 'city', 'commune']

class UserEmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEmployer
        fields = ['id', 'user', 'address', 'phone_number', 'post']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        user_employer = UserEmployer.objects.create(user=user, **validated_data)
        return user_employer
class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ['id', 'user_employer', 'code', 'created_at']

