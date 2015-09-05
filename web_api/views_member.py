from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers, pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib import auth

class Login(APIView):

    def post(self, request):

        if request.user.is_authenticated():
            return render(request, 'money/base.html')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return render(request, 'money/base.html')
        else:
            return render(request, 'money/base.html')
