"""
Views for the user API.
"""
from rest_framework import generics

from user.serializer import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Cerate a new user in the system."""
    serializer_class = UserSerializer
