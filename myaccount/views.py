from django.shortcuts import render
from mainContent.models import poolDetails , addMembers

# Create your views here.   

def account(request):

    poolVal = addMembers.objects.filter(roll_no = request.user.username)
    print(poolVal)
    #poolValues = None
    poolValues = []
    for val in poolVal:
        poolValues = poolDetails.objects.filter(poolId = val.poolId)
    
    print(poolValues)
    return render(request,'account.html',{'values':poolValues})
