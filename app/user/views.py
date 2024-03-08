"""
Viewvs for the user API
"""
from rest_framework import generics
from user.serializers import UserSerliazer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerliazer
