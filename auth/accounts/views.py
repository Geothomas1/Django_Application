from django.shortcuts import render
from accounts.models import Register
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        Register.objects.filter(
            email=request.POST['email'], password=request.POST['password']).exists()
        user = Register.objects.get(
            email=request.POST['email'], password=request.POST['password'])
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user = Register(
            name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
        user.save()
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')

# def dashboard(request):
#     return render('dashoard.html')
