from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from .serializers import LogoutSerializer, UserSerializer, TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated

class Loggedin(generics.ListCreateAPIView):

    permission_classes = [ IsAuthenticated ]

    def get(self, request, **kwargs):
        print(request.user)
        return render(request, 'users/loggedin.html')

class RegisterView(APIView):
    http_method_names = ['post', 'get']

    def get(self, request):
        return render(request, 'users/register.html') 

    def post(self, *args, **kwargs):
        data = self.request.POST
        print(data)
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            if data.get('password') == data.get('password2'):
                get_user_model().objects.create(**serializer.validated_data)
                return HttpResponseRedirect('http://127.0.0.1:8000/login/')
            else:
                return Response("Passwords not matching") 
            
        return Response(status=HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def get(self, request, *args, **kwargs):
        return render(request, 'users/login.html')

class LogoutAPIView(generics.ListCreateAPIView):

    permission_classes = [ IsAuthenticated ]

    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid()
        serializer.save() 

        return Response(status = status.HTTP_204_NO_CONTENT)

