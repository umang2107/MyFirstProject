from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from home.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable" : "abhi is web developer",
    }
   # return HttpResponse("this is homepage....")
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is aboutpage....")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is servicespage....")

def contact(request):
    if request.method == "post":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobileno = request.POST.get('mobileno')
        password = request.POST.get('password')
        Contact = contact(name=name, email=email, mobileno=mobileno, password=password, date=datetime.today())
        contact.save()
        messages.success(request, 'your entry has been done')

        def __str__(self):
            return self.name
            
        
    return render(request, 'contact.html')
    #return HttpResponse("this is contactpage....")