from django.urls import path

from budget_management.users.views import SignupView

urlpatterns = [
    path("signup", SignupView.as_view(), name="signup"),
]
