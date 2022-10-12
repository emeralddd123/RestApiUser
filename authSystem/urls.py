"""authSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from dj_rest_auth.registration.views import ResendEmailVerificationView, RegisterView, VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.views.generic import TemplateView
from allauth.account.views import email_verification_sent
from .mod_views import Mod_ResendEmailVerificationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', RegisterView.as_view(),name='rest_register'),
    path('auth/registration/account-confirm-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    re_path(r'^auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),name='account_confirm_email'),
    path("auth/registration/account-confirm-email/",email_verification_sent,name="account_email_verification_sent"),
    path('auth/registration/resend-email/', Mod_ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    path('auth/password/reset/confirm/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    
]

