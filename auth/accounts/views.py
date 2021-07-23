from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Register
from .serializers import RegisterSerializer


class registerUserList(APIView):
    def get(self, request):
        users = Register.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)

    def post(self):
        pass

# Create your views here.


# def index(request):
#     return render(request, 'index.html')


# def login(request):
#     if request.method == 'POST':
#         Register.objects.filter(
#             email=request.POST['email'], password=request.POST['password']).exists()
#         user = Register.objects.get(
#             email=request.POST['email'], password=request.POST['password'])
#         return render(request, 'dashboard.html')
#     else:
#         return render(request, 'login.html')


# def register(request):
#     if request.method == 'POST':
#         user = Register(
#             name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
#         user.save()
#         return render(request, 'login.html')
#     else:
#         return render(request, 'register.html')

# def dashboard(request):
#     return render('dashoard.html')
