from django.shortcuts import render
from django.contrib.auth.models import User,auth

from .models import poolDetails , addMembers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import date


# Create your views here.

def home(request):
    return render(request,"home.html")

def pools(request):
    values = poolDetails.objects.all() 
    print(values)  
    return render(request, 'pools.html' , {"values":values})

def chat(request):
    present_user = User.objects.all()
    
    return render(request,'ChatAppUI.html',{"values":present_user})

def searching(request):
    element = request.POST['search']
    element.lower()
    values = poolDetails.objects.all()
    #values1 = poolDetails.objects.filter(dest=element) 
    poss = []
    #print(element)
    for value in values:
        #print(value.dest)
        if value.dest.lower() == element :
            #print(value.time,element)
            poss.append(value)

    return render(request, 'pools.html' , {"values":poss})

def poolsForm(request):
    return render(request,"poolsForm.html")

def addDetails(request):
    
    name = request.user.first_name
    rollNo = request.user.username
    stloc = request.POST['stloc']
    dest = request.POST['dest']
    date1 = request.POST['date']
    time1 = request.POST['time']
    mode = request.POST['mode']
    maxPPL = request.POST['NoOfPpl']

    lastObj = poolDetails.objects.all().last()
    if lastObj == None:
        pId = 0
    else:
        pId = lastObj.poolId
    pId += 1
    obj = poolDetails(name=name, rollNo=rollNo,stloc=stloc,dest=dest, poolDate=date1, poolTime=time1,mode=mode,maxPPL=maxPPL,poolId=pId,count=1)
    obj.save()
    obj1 = addMembers(poolId=pId,name=name,roll_no=rollNo)
    obj1.save()
    
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    
    values = poolDetails.objects.all()
   
    return render(request, 'pools.html' , {"values":values})

def addToPool(request,value):
   
    poolValues = poolDetails.objects.filter(poolId = value)
    
    for val in poolValues:        
        
        obj = addMembers(poolId=val.poolId,name=request.user.first_name,roll_no=request.user.username)
        obj.save()
        val.count = val.count + 1
        val.save()
        break
    
    values = poolDetails.objects.all()
    added = True
    return render(request, 'pools.html' , {"values":values,"add":added})
    
def viewMembers(request, value):
    poolValues = addMembers.objects.filter(poolId = value)

    return render(request,'poolMembers.html' , {"values":poolValues})