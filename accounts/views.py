from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import AllowAny

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] 
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully", "user": {"email": user.email, "username": user.username, "role":user.role}}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
