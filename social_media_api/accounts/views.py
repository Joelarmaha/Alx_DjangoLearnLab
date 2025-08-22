from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model
from accounts.models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView
from .models import User
from .serializers import UserPublicSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class IsAuthenticatedOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class FollowUserView(APIView):
    permission_classes = [IsAuthenticatedOnly]

    def post(self, request, user_id):
        target = get_object_or_404(User, pk=user_id)
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.follow(target)
        return Response({"detail": f"You are now following {target.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticatedOnly]

    def post(self, request, user_id):
        target = get_object_or_404(User, pk=user_id)
        if target == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.unfollow(target)
        return Response({"detail": f"You have unfollowed {target.username}."}, status=status.HTTP_200_OK)


class ListFollowingView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOnly]
    serializer_class = UserPublicSerializer

    def get_queryset(self):
        return self.request.user.following.all().order_by("username")


class ListFollowersView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOnly]
    serializer_class = UserPublicSerializer

    def get_queryset(self):
        return self.request.user.followers.all().order_by("username")
