from rest_framework_simplejwt.views import TokenVerifyView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views


urlpatterns = [
    
    path('create-group', views.CreateGroups.as_view(), ),
    path('list-group', views.GetGroups.as_view(), ),
    path('group-enter/<int:groups>', views.GroupEnterView.as_view(), ),
    path('show-comments', views.ShowComments.as_view(), ),
    path('post-like', views.LikePost.as_view(), ),
    

    

    
     
]