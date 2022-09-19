from rest_framework_simplejwt.views import TokenVerifyView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


urlpatterns = [
    
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup',views.Signup.as_view()),
    path('otp_login',views.otp_login.as_view()),
    path('verify_otp',views.otp_verify.as_view()),
    path('si',views.CreateDocAPIView.as_view()),
    path('nice',views.Verifyss.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  


    
    
]