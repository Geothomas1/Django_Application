from rest_framework import serializers
from .models import Register
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        #filed=['name','email']
        fields='__all__'