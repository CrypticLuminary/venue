from django.urls import path
from .views import login_view,signin_view

urlpatterns = [
    path('', login_view, name='login'),  # URL pattern for the login view
    # path('', signin_view, name='signin'),  # URL pattern for the login view
]
