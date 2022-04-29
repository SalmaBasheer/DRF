from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,BlogpostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blogpost

class BlogpostListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

def get(self, request, *args, **kwargs):
        '''
        List all the blogpost items for given requested user
        '''
        Blogpost= Blogpost.objects.filter(user = request.user.id)
        serializer = BlogpostSerializer(Blogpost, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)


def post(self, request, *args, **kwargs):
        '''
        Create the Blogpostwith given todo data
        '''
        data = {
            'blogid': request.data.get('blogid'), 
            'Title': request.data.get('Title'), 
            'user': request.user.id
        }
        serializer = BlogpostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]})
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

# Create your views here.
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
        
