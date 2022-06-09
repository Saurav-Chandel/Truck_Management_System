from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .helpers import *
import requests
# Create your views here.




class SignUpView(APIView):
    '''
    SignUp API
    '''
    permission_classes=[AllowAny,]
    authentication_classes = []

    def post(self,request):
        data=request.data
        print(data)
        username=request.data.get('email')
        data['username']=username

        if User.objects.filter(email=data['email']).exists():
            return Response({'msg':'User already exists.'})
       
        #Add User data
        serializer=SignUpSerializer(data=data)    
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        d=dict()
        d['User']=str(user.id)
        d['DeviceToken']=data.get("DeviceToken","")
        d['DeviceType']=data.get("DeviceType","")
        Devices.objects.filter(DeviceToken=d["DeviceToken"]).delete()

        #Add Device data
        deviceserializer=DeviceSerializer(data=d)
        deviceserializer.is_valid(raise_exception=True)
        deviceserializer.save()

        # create a token on the basis of email and password.
        url='http://localhost:8000/user/api/token/'
        email=request.data.get('email')
        payload={'username':email,'password':request.data['password']}
        response = requests.request("POST", url, data=payload)
        token=response.json()

        # my_dict2 = {k: v for k, v in data.items() if k != 'phone_otp'}  #exclude phone-otp from data.items()

        return Response({'data':data,'token':token,'msg':'signup successfully'})



        