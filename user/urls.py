from django.urls import path,include
from .views import (
    UserRegisterView, UserLoginView, UserLogoutView,
    ProfileCreateView, ProfileDetailView
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('account/', include('django.contrib.auth.urls')),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('profile/', ProfileDetailView.as_view(), name='profile_view'),
]