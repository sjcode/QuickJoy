# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from account.serializers import UserSerializer, GroupSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
import json
# Create your views here.

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def login(request):
    retData = {'result' : True}
    return HttpResponse(json.dumps(retData), content_type="application/json")

def logout(request):
    retData = {'result' : True}
    return HttpResponse(json.dumps(retData), content_type="application/json")

def register(request):
    retData = {'result' : True}
    return HttpResponse(json.dumps(retData), content_type="application/json")

def profile(request):
    retData = {'result' : True}
    return HttpResponse(json.dumps(retData), content_type="application/json")

def settings(request):
    retData = {'result' : True}
    return HttpResponse(json.dumps(retData), content_type="application/json")




