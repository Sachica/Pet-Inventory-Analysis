from django.shortcuts import render,redirect
from django import views
from .models import Pet
# Create your views here.

class dashboard(views.View):

        def get(self, request):
            pets = Pet.objects.all()
            return render(request, 'pets/dashboard.html',{'pets':pets})

        def post(self, request):
            name = request.POST['name']
            species = request.POST['species']
            age = request.POST['age']
            quantity = request.POST['quantity']
            print(request)
            Pet.objects.create(name=name, species=species, age=age, quantity=quantity)    
        
            return redirect('/pets/dashboard')


class eliminarPets(views.View):
    
            def get(self, request, id):
                pet = Pet.objects.get(id=id)
                pet.delete()    
                return redirect('/pets/dashboard')

class editarPets(views.View):

            def get(self, request, id):
                pet = Pet.objects.get(id=id)
                return render(request, 'pets/editarPet.html',{'pet':pet})

            def post(self, request):

                pet = Pet.objects.filter(id=request.POST['id']).first()
                print(pet)
                pet.name = request.POST['name']
                pet.species = request.POST['species']
                pet.age = request.POST['age']
                pet.quantity = request.POST['quantity']
                pet.save()
                return redirect('/pets/dashboard')