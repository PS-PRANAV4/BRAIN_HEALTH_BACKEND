
import json
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import AccountSerializer, DocSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from twilio.rest import Client
from .models import Accounts
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework import serializers
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from Brain_Health import settings
import jwt
# Create your views here.

class Signup(APIView):

    
    def post(self,request,*args,**kwargs):
        user = request.user
        print(user)
        data = request.data
        if 'certi' in request.data:
            print('hello')
            print(request.data['certi'])
        serializer =  DocSerializer(data=data, context={'request': request})
        
        if serializer.is_valid():
            
            serializer.save()
            return JsonResponse('user is  created',safe=False)

        # data = MultiPartParser().parse(request)
        # print(data)
        # data = JSONParser().parse(request)
        # print(data)
        
        print(request)
        
         
        
        # data = request.POST['file']
        
        # print(data)
        # user_serializer = DocSerializer(data=request.data)
        # print(user_serializer)
        # if user_serializer.is_valid():
        #     user_serializer.save()
        #     return JsonResponse('user created',safe=False)
        # else:
        return JsonResponse('user is not created',safe=False)

class otp_login(APIView):
    def post(self,request):
        print(request.POST)
        data = JSONParser().parse(request)
        print(data)
        number = data['phone_number']
        print(number)
        try :
            user = Accounts.objects.get(phone_number = number)
        except: 
            return JsonResponse("phone number doesn't exist",safe=False)
        
        print(number) 
        account_sid = 'AC19ac143574cb2d7ec98fc7f98c0dd92c'
        auth_token = '23d143f73033b7c826e7d04033c3e94d'
        client = Client(account_sid, auth_token)

        verification = client.verify \
                     .services('VA7a7b213770440143ef193203f8bec694') \
                     .verifications \
                     .create(to= f"+91{number}", channel='sms')

        print(verification.status)
        val = {"email":user.email}
        return JsonResponse(val)
    
class otp_verify(APIView):
    def post(self,request):
        data = JSONParser().parse(request)
        email = data['email']
        print(email)
        print(data)
    
    
        user = Accounts.objects.get(email = email)
        number = user.phone_number
        codes = data['code']
        account_sid = 'AC19ac143574cb2d7ec98fc7f98c0dd92c'
        auth_token = '23d143f73033b7c826e7d04033c3e94d'
        client = Client(account_sid, auth_token)

        verification_check = client.verify \
                            .services('VA7a7b213770440143ef193203f8bec694') \
                            .verification_checks \
                            .create(to=f"+91{number}", code=codes) 

        print('login')
        refresh = AccessToken.for_user(user)
        access = RefreshToken.for_user(user)
        print(refresh)
        val = {'access':str(refresh),'refresh':str(access)}

        return JsonResponse(json.dumps(val),safe=False)


class CreateDocAPIView(APIView):

    # permisssion_classes = (IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        user = request.user

        data = request.data
        name = data['user']
        user = json.loads(name)
        
        
        serializer =  DocSerializer(data=data, context={'request': request})
        
        
        if serializer.is_valid():
            users = Accounts.objects.create_user(username=user['username'],phone_number=user['phone_number'],email=user['email'],first_name=user['first_name'],last_name=user['last_name'],designation=user['designation'],password=user['password'])
            print('nice')
            serializer.save(owner=users)
            return Response({'success' :'True','message' : 'Doc created successfully','data' : serializer.data},status=200)
        return Response(serializer.errors,status=400)


class Verifyss(APIView):
    permission_classes = []
    authentication_classes = []
    
    def post(self,request,*args,**kwargs):
        data = request.data
        token = data['token']
        
        tokens = str(token)
        try:
            user_jwt = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(user_jwt['user_id'])
            user = Accounts.objects.get(id=user_jwt['user_id'])
            val = {'username':user.username, 'status':'true'}
            return JsonResponse(val,safe=False)
        except Exception as e:
            val = {'status':'false'}
            return JsonResponse(val,safe=False)