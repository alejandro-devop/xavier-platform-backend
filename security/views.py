from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer


class RegisterAPI(generics.GenericAPIView):
    """
    Api to register new users
    """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Method to register users
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user, context=self.get_serializer_context()).data)
