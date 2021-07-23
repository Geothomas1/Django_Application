from django.db.models.fields import AutoField
from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'
        AutoField
