from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from rest_framework import status

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User, Role, Camera, Schedule, NotificationDevice, Notification

from .serializers import (
    UserCreateSerializer, 
    UserLoginSerializer,
    UserProfileSerializer,
    RoleSerializer, 
    CameraSerializer,
    GoogleTokenSerializer,
    ScheduleSerializer,
    ScheduleSignalSerializer,
    NotificationDeviceSerializer,
    NotificationSerializer,
    ViewerSerializer)

from rest_framework import generics

from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


# user register
class UserRegister(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


# login
class UserLogin(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserProfile(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


# perform create: add user when create camera with token in POST request
# list : filter cameras by request user in GET request
class CameraList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

    def perform_create(self, serializer):
        serializer.save(uid=self.request.user)

    def list(self, request):
        queryset = Camera.objects.filter(uid=request.user)
        serializer = CameraSerializer(queryset, many=True)
        return Response(serializer.data)


class CameraDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class GoogleToken(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = GoogleTokenSerializer

    # def update(self, request, *args, **kwargs):
    #     queryset = User.objects.filter(id=request.user.id)
    #     serializer = GoogleTokenSerializer(queryset, *args)
    #     return Response(serializer.data, status=HTTP_200_OK)


class ScheduleCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ScheduleDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Schedule.objects.all().select_related('user')
    serializer_class = ScheduleSerializer
    lookup_field = 'user__username'


class ScheduleSignal(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Schedule.objects.all().select_related('user')
    serializer_class = ScheduleSignalSerializer
    lookup_field = 'user__username'


class NotificationDevice(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NotificationDevice.objects.all()
    serializer_class = NotificationDeviceSerializer


class NotificationDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = 'user__username'


class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# get, update, delete role with role_id
# api/role/(?P<pk>[0-9]+)/ , put method need to have ending /
class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer  
   

# class Viewer(generics.ListCreateAPIView):
#     queryset = Viewer.objects.all()
#     serializer_class = ViewerSerializer
