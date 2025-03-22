import sys
from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from library.serializers import UserSerializer, UserRegisterSerializer


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserRegisterViewSet(ViewSet):
    """
    API endpoint that allows a user to be registered.
    """
    permission_classes = [permissions.AllowAny]

    def create(self, request, format=None, methods='POST'):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(
                email=serializer.validated_data['email'],
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(
                {'message': 'User has been registered successfully'}
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )