from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from budget_management.users.views import SignupView

urlpatterns = [
    path("signup", SignupView.as_view(), name="signup"),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
