from django.urls import path, include,re_path
from dj_rest_auth.registration.views import  RegisterView, VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.views.generic import TemplateView
from allauth.account.views import email_verification_sent 
from .views import Mod_ResendEmailVerificationView, Mod_PasswordResetView, CustomPasswordResetView

from .socialviews import GoogleLogin

urlpatterns = [
    path('auth/password/reset/', Mod_PasswordResetView.as_view(), name='rest_password_reset'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', RegisterView.as_view(),name='rest_register'),
    path('auth/registration/account-confirm-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    re_path(r'^auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),name='account_confirm_email'),
    path("auth/registration/account-confirm-email/",email_verification_sent,name="account_email_verification_sent"),
    path('auth/registration/resend-email/', Mod_ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    path('auth/password/reset/confirm/<str:uidb64>/<str:token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    #social login
    path('auth/google/', GoogleLogin.as_view(), name='google_login')
    
]

