from django.urls import path
from . import views


urlpatterns = [
    path('createuser/', views.ListCreateUser.as_view(), name='createuser'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('list/<int:pk>/', views.RetrieveUser.as_view(), name='retrieveuser'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]