from django.shortcuts import render
from signup.serializers import NewUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from signup.models import NewUser

# Create your views here.
class Account(APIView):
	def get(self, request, format=None):
		newUsers = NewUser.objects.all()
		serializer = NewUserSerializer(newUsers, many=True)
		return Response(serializer.data)
		
	def put(self, request, format=None):
		serializer = NewUserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(APIView):
	def get(self, request, format=None):
		return Response(status=status.HTTP_400_BAD_REQUEST)
	
	