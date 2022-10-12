from allauth.account.models import EmailAddress
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from dj_rest_auth.registration.serializers import  ResendEmailVerificationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _



class Mod_ResendEmailVerificationView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ResendEmailVerificationSerializer
    queryset = EmailAddress.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = EmailAddress.objects.filter(**serializer.validated_data).first()
        if email and not email.verified:
            email.send_confirmation(request)
        elif not email:
            return Response({'detail': _('No Account was found with this email')}, status=status.HTTP_404_NOT_FOUND)
        elif email.verified:
            return Response({'detail': _('Email has been verified already')}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': _('ok')}, status=status.HTTP_200_OK)
    
