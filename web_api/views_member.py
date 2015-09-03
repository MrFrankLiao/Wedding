from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers, pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

class Login(APIView):

    def get(self, request):
        return Response(123)
