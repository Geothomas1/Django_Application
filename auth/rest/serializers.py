from django.db.models import fields
from accounts.models import Register
from rest_framework import serializers

class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    model=Register
    fields=['name','email','password']