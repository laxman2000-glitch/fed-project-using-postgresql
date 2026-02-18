from django.shortcuts import render
from.models import Contact

# Create your views here.
def register(request):
    message= None
    if request.method=="POST":
        name = request.POST.get('name')
        father = request.POST.get('father')
        number = request.POST.get('number')
        pincode = request.POST.get('pincode')

        Contact.objects.create(
            name= name,
            father= father,
            number=number,
            pincode=pincode,   
        )
        message='register sucessful'
    return render(request,'register.html',{'message':message})

    