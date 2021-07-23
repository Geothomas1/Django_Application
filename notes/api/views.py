from django.db.models import manager
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from api import serializers


@api_view(['GET'])
def getRoute(request):
    routes = [
        {
            'name': 'Geo Thomas',
            'age': '23',
            'place': 'Kottayam'
        },
        {
            'name': 'Manuel Rober',
            'age': '23',
            'place': 'Eranakulam'
        },
        {
            'name': 'Joseph John',
            'age': '23',
            'place': 'Kottayam'
        },

    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNotesbyId(request, pk):
    id = Note.objects.get(id=pk)
    serializer = NoteSerializer(id, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data
    createbody = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(createbody, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNotebyId(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note is deleted")
