from django.urls import path
from .views import VerifyAadhaarView

urlpatterns = [
    path('verify/', VerifyAadhaarView.as_view(), name='verify-aadhaar')
]