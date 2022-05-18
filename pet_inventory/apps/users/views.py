from django.shortcuts import redirect, render
from django import views
from .models import User
from django.contrib.auth import authenticate
from ..pets.views import dashboard
from django.contrib.auth.hashers import make_password
# Create your views here.


class index(views.View):

    def get(self, request):
        return render(request, 'users/index.html')
    


class iniciarSesion(views.View):
    
    def get(self, request):
        return render(request, 'users/iniciarSesion.html')
    
    def post(self, request):
        print(request.POST)
        username = request.POST['txtUsername']
        password = request.POST['txtPassword']
        user = authenticate(username=username, password=password)
        print(user)

        if user is None :
            return render(request, 'users/index.html')
        else :   
             return redirect('/pets/dashboard')

class registrarUsuario(views.View):
        
        def post(self, request):
            username = request.POST['username']
            email = request.POST['email']
            password = make_password(request.POST['password'])
            User.objects.create(username=username, email=email, password=password)
            return redirect('/pets/dashboard')
            