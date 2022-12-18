from django.shortcuts import render
from django.http import HttpResponse
from . models import Person
from django.views import View

# def home(request):    
#     person_data = PersonDetails.objects.all()
 
#     return render(request, 'home.html', {"person_data":person_data})

class Register(View):
    def get(self,request,  *args, **kwargs):
        try:
            return render(request, 'register.html')
        except:
            pass

    def post(self,request,  *args, **kwargs):
        try:
            if request.method=='POST':
                first_name = request.POST['first_name']
                last_name =request.POST['last_name']
                email=request.POST['email']
                password=request.POST['password']
                conpass=request.POST['conpass']
                if password == conpass:
                    if not Person.objects.filter(email=email):
                        inst = Person(first_name=first_name,last_name=last_name,email=email,password=password)
                        inst.save()                        
                    # return HttpResponse("User Register SuccessFully")
                        return render(request, 'login.html')
            
                
        except:
            pass



class Login(View):
    def get(self,request, *args, **kwargs ):
        try:
            return render(request, 'login.html')
        except:
            pass
        

    def post(self,request,  *args, **kwargs):
        try:
            if request.method == 'POST':
                email = request.POST['email']
                password = request.POST['password']
                if Person.objects.filter(email=email,password=password):
                    return HttpResponse("user logged in sucessfylly")
            # return render(request, 'login.html')
        except:
            pass






