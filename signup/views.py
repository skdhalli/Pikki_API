from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from signup.models import NewAccount
import json

# Create your views here.
class Account(APIView):
	def put(self, request, format=None):
		newAccount = NewAccount(request.data["Request"])
		response = newAccount.Save()
		return Response(json.dumps(response), status=status.HTTP_201_CREATED)

class AccountDetail(APIView):
	def get(self, request, format=None):
		return Response(status=status.HTTP_400_BAD_REQUEST)
	
	