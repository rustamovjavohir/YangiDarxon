from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from bot.views import *

urlpatterns = [
    path("", SendMessageView.as_view(), name='send-message-bot'),
]
