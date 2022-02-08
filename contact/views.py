from django.shortcuts import render
from .models import contact

# Create your views here.

def contacts(request):
    return render(request,"contact.html")

def submitQuery(request): 
    name = request.POST['name']
    email = request.POST['email']
    query = request.POST['query']

    obj = contact(name=name,email=email,query=query)
    obj.save()
    msg = "Thank you for submitting your response, our team will soon contact you !"
    return render(request,"contact.html",{"values":msg})

