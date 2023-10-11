from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from rest_framework import generics,status, views
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from jwt import decode, ExpiredSignatureError, DecodeError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import RegisterSerializer,EmailVerificationSerializer,LoginSerializer
from .models import User
from .utils import Util


class RegisterView(generics.GenericAPIView):
    
    serializer_class =RegisterSerializer
    permission_classes=[]
    
    # ISSUE::
    # should type post method not Post as if write Post it will not work
    def post(self,request:Request):
        user = request.data
        serializer= self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        
        user_data=serializer.data
        
        
        user= User.objects.get(email=user_data['email'])
        access_token=RefreshToken.for_user(user).access_token
        
        # TODO:: send Email to verify user
        # access_token= RefreshToken.for_user(user).access_token
        # current_site_domain=get_current_site(request).domain
        # relativeLink=reverse('email-verify')
        
        # absurl='http://'+current_site_domain+relativeLink+"?token="+str(access_token)
        
        # email_body= 'Hi'+user.username+'use below link to verify your email \n'+absurl
        # data={
        #     "email_subject":'Verify your email',
        #     "email_body":email_body,
        #     "to_email":user.email
        # }
        # Util.send_email(data)
        data={
            'user_data':user_data,
            'access_token':str(access_token)
        }
        return Response(data,status=status.HTTP_201_CREATED)
        
class VerifyEmail(views.APIView):
    serializer_class=EmailVerificationSerializer
    #NOTE::
    # used to add token to params within swagger documentation
    token_param_config=openapi.Parameter('token',in_=openapi.IN_QUERY,description='Enter user acces Token',type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self,request):
        token = request.GET.get('token')
        if not token:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            #ISSUE::
            # should add algorithm for decoding as the default algorith for jwt encoding is HS256
            # or it will always gives us Invalid Token  
            
            payload= decode(token,settings.SECRET_KEY,algorithms=['HS256'])
            user_id = payload.get('user_id')
            if not user_id:
                return Response({'error': 'Invalid token payload'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(id=user_id)
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)

        except ExpiredSignatureError:
            return Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)

        except DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data,status=status.HTTP_200_OK)