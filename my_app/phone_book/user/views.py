from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
def login(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        if not bool(request.data):
            return  HttpResponseBadRequest('Please provide credentials.')
        username= request.data.get("usename")
        password=request.data.get("password")
        if username is not None or password is not None:
            user = authenticate(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"Token": token.key}, status=status.HTTP_200_OK)
        else:
            return HttpResponseNotFound('Invalid credentials.')

