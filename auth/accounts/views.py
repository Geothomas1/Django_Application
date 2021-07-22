from django.shortcuts import render
# Create your views here.


def indexView(request):
    return render(request, 'index.html')


def indexLogin(request):
    return render(request, 'login.html')


def indexRegister(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
    else:
        return render(request, 'register.html')
