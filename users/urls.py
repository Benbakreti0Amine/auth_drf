# from django.urls import path
# from . import views


# urlpatterns = [
#     path('createuser/', views.ListCreateUser.as_view(), name='createuser'),
#     path('login/', views.LoginView.as_view(), name='login'),
#     path('list/<int:pk>/', views.RetrieveUser.as_view(), name='retrieveuser'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),
# # user emp
#     path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),

#     path('employers/', views.UserEmployerListCreateView.as_view(), name='user-employer-list-create'),
#     path('qrcodes/', views.QRCodeListCreateView.as_view(), name='qrcode-list-create'),


# ]



from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet, 
    PostViewSet, 
    UserEmployerViewSet, 
    QRCodeViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'user-employers', UserEmployerViewSet, basename='user-employer')
router.register(r'qrcodes', QRCodeViewSet, basename='qrcode')

urlpatterns = [
    path('', include(router.urls)),
]
