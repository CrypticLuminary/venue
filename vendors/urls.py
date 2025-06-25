from django.urls import path
from .views import homeDetail

urlpatterns = [
    path('', homeDetail.as_view() ,name="home")

]
