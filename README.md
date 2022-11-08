THIS IS AN DJANGO PROJECT THAT HANDLES USER REGISTERATIONS AND LOGIN AND OTHER USER FUNCTIONALITIES LIKE PASSWORD RESET, EMAIL CONFIMATION IN REST API METHOD.

THE PROJECT IS BASED ON REST_FRAMEWORK, DJ_REST_AUTH AND ALLAUTHS  

START A DJANGO PROJECT 

PIP INSTALL THE PAKCKAGES IN REQUIREMETS.TXT FILE
ADD THHE FOLLOWING TO INSTALLED APPS

    'allauth',
    'allauth.account',
    'allauth.socialaccount',   
    'allauth.socialaccount.providers.google',
    
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',

ADD 'authApp' TO DJANGO INSTALLED APPS

THEN ADD THE FOLLOWING CONFIGURATIONS TO sttings.py IN YOUR PROJECT FOLDER


REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )
    
}

REST_AUTH_SERIALIZERS = {
    #'LOGIN_SERIALIZER': 'authSystem.mod_serializers.Mod_LoginSerializer',
        
    'REST_USE_JWT': True,
    
    'OLD_PASSWORD_FIELD_ENABLED' : True
    
    
}

REST_USE_JWT = True

JWT_AUTH_COOKIE = 'my-app-auth'

JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

ACCOUNT_EMAIL_REQUIRED=True

#to be able to login with either email or username or both with password 
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_CONFIRM_EMAIL_ON_GET = True

#to avoid signing up with invalid email
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 180

OLD_PASSWORD_FIELD_ENABLED = True

ACCOUNT_FORMS = {'reset_password': 'authApp.forms.MyCustomResetPasswordForm'}
