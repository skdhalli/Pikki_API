from rest_framework import serializers
from signup.models import NewUser

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('username', 'email', 'password')

	def save(self, validated_data):
		#save to ES