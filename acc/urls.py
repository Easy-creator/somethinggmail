from django.urls import path
from .views import gmail_picker, gmail_otp


urlpatterns = [
    path('', gmail_picker, name='gmail_picker'),
    path('otp/', gmail_otp, name='otp')
]

# gmail_login