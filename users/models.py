# from django.db import models
# from django.core.validators import RegexValidator
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class MyUserManager(BaseUserManager):

#     def create_user(self, username, email,first_name,last_name, password, **kwags):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')
#         if not first_name:
#             raise ValueError('Users must have a firstname')
#         if not last_name:
#             raise ValueError('Users must have a lastname')

#         user = self.model(
#             username=username,
#             email=self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#         )

#         user.is_active  = True
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email,first_name,last_name, password):
#         user = self.create_user(username=username,email=email, password=password,first_name=first_name,last_name=last_name)

#         user.is_staff = True
#         user.is_superuser = True
#         user.set_password(password)
#         user.save()
#         return user 

# class User(AbstractBaseUser, PermissionsMixin):

#     alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')
#     username    = models.CharField(unique=True, max_length=20, validators=[alphanumeric])
#     email       = models.EmailField(verbose_name='email address', unique=True, max_length=244)
#     first_name  = models.CharField(max_length=30, null=True, blank=True)
#     last_name   = models.CharField(max_length=50, null=True, blank=True)
#     is_active   = models.BooleanField(default=True, null=False)
#     is_staff    = models.BooleanField(default=False, null=False)
#     # image = models.ImageField(upload_to='images/', default='images/default_profile.jpg')
#     # token = models.CharField(max_length=255, default="",blank=True, null=True)

#     objects = MyUserManager()

#     USERNAME_FIELD  = 'email'
#     REQUIRED_FIELDS = ['username','last_name','first_name']

#     def get_full_name(self):
#         fullname = self.first_name+" "+self.last_name
#         return self.fullname

#     def get_short_name(self):
#         return self.username

#     def str(self):
#         return self.email
    


# # models for the user employeur


# class Post(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     commune = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.name} - {self.city}, {self.commune}"

# class UserEmployer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
#     address = models.TextField()
#     phone_number = models.CharField(max_length=15)
#     post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='employers')

#     def __str__(self):
#         return f"{self.user.get_full_name()} - {self.company_name} ({self.post.name if self.post else 'No Post'})"

# class QRCode(models.Model):
#     user_employer = models.ForeignKey(UserEmployer, on_delete=models.CASCADE, related_name='qr_codes')
#     code = models.CharField(max_length=100, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"QR Code for {self.user_employer.user.get_full_name()} at {self.user_employer.post.name if self.user_employer.post else 'No Post'}"

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class UserEmployer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.email} - {self.company_name}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class QRCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qrcodes')
    code = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"QR Code for {self.user.email}"