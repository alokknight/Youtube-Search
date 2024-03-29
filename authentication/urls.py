from django.urls import path, include

from .views import (
    LogoutAPIView,
    RegisterView,
    VerifyEmail,
    LoginAPIView,
    RequestPasswordResetEmail,
    PasswordTokenCheckAPI,
    SetNewPasswordAPIView,
    OwnerListView,
    OwnerUpdateRetriveDeleteView,
    UserViewSet,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path("api/",include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("email-verify/", VerifyEmail.as_view(), name="email-verify"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path(
        "request-reset-email/",
        RequestPasswordResetEmail.as_view(),
        name="request-reset-email",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordTokenCheckAPI.as_view(),
        name="password-reset-confirm",
    ),
    path(
        "password-reset-complete",
        SetNewPasswordAPIView.as_view(),
        name="password-reset-complete",
    ),
    path("profile/", OwnerListView.as_view(), name="profile"),
    path("profile/<int:pk>", OwnerUpdateRetriveDeleteView.as_view(), name="profile"),
]
