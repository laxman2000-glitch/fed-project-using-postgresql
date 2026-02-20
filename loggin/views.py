from django.shortcuts import render
from.models import Contact
from django.http import JsonResponse
import json

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

def user_get(request):
    if request.method == 'GET':
        data = Contact.objects.all().values()
        return JsonResponse(list(data),safe=False,status=200)

def user_post(request):
    if request.method=="POST":
        body = json.loads(request.body)

        name= body.get('name')
        father= body.get('father')
        pincode= body.get('pincode')

        if not name or not father or not pincode :
            return JsonResponse({
                "message": "need fields completly"
            }, status=400)
        contact= Contact.objects.create(
            name=name,
            father=father,
            pincode=pincode,
        )
        return JsonResponse({
            "message": "sucessfully uploaded",
            "user ID": contact.id,
        }, status=201)
    return JsonResponse({
        "message": "invalid request POST "
    },status=405)

def user_patch(request):
    if request.method=="PATCH":
        body= json.loads(request.body)

        contact_id = body.get('id')
        name = body.get('name')
        father=body.get('father')
        pincode=body.get('pincode')

        if not contact_id:
            return JsonResponse({
                "message": "need user_id"
            },status=400)

        if Contact.objects.filter(id=contact_id).exists():
            contact= Contact.objects.get(id=contact_id)
            if name:
                contact.name=name
            if father:
                contact.father=father
            if pincode:
                contact.pincode=pincode

            contact.save()

            return JsonResponse({
                "message":"updated fields sucessful"
            }, status=201)
        else:
            return JsonResponse({"message":"invalid id"},status=400)

        return JsonResponse({
        "message": "invalid http request"
    },status=405)
def user_put(request):
    if request.method == "PUT":
        body= json.loads(request.body)

        contact_id = body.get('id')
        name= body.get('name')
        father=body.get('father')
        pincode=body.get('pincode')

        if not contact_id:
            return JsonResponse({
                "message":"user ID not provided"
            },status=400)
        if Contact.objects.filter(id=contact_id).exists():
            contact= Contact.objects.get(id=contact_id)

            contact.name=name
            contact.father=father
            contact.pincode=pincode

            contact.save()
            return JsonResponse({
                "message": "fields changed appiled"
            }, status= 201)
        else:
            return JsonResponse({
                "message":"user ID don't exist"
            },status=400)
        return JsonResponse({
        "message":"invalid http request"
    },status=405) 
def user_delete(request):
    if request.method == "DELETE":
        body= json.loads(request.body)
        contact_id=body.get('id')

        if not contact_id:
            return JsonResponse({
                "message":"user ID not provided"
            },status=400)

        if Contact.objects.filter(id=contact_id).exists():
            Contact.objects.filter(id= contact_id).delete()

            return JsonResponse({
                "message":"user details deleted sucessfull"
            },status=201)
        else:
            return JsonResponse({
                "message":"user ID not exists"
            },status=400)
        return JsonResponse({
        "message":"invalid http request"
    },status=405)
def student(request):
    if request.method=="POST":
        body = json.loads(request.body)

        name = body.get('name')
        father=body.get('father')
        pincode=body.get('pincode')

        if not name or not father or not pincode:
            return JsonResponse({
                "meassage":"got empty fields"
            },status=400)
        contact=Contact.objects.create(
            name= name,
            father=father,
            pincode=pincode,
        )
        return JsonResponse({
            "message":"succeful uploaded",
            "user_id": contact.id,
            },status=200)
     
    elif request.method == "PUT":
        body=json.loads(request.body)

        user_id=body.get('user_id')
        name=body.get('name')
        father=body.get('father')
        pincode=body.get('pincode')

        if not user_id :
            return JsonResponse({
                "message": "User_id should not be empty"
            },status=400)
        if Contact.objects.filter(id=user_id).exists():
            contact = Contact.objects.get(id=user_id)
            Contact.object.create(
                name=contact.name,
                father=contact.father,
                pincode=contact.pincode,
            )
            return JsonResponse({
                "message":"succesfully updated all fields"

            },status=200)
    elif request.method =="DELETE":
        body= json.loads(request.body)

        user_id=body.get('user_id')
        name=body.get('name')
        father=body.get('father')
        pincode=body.get('pincode')

        if not user_id:
            return jsonResponse({
                "message":"User_id should not be empty",
            },status=400)
        if Contact.objects.filter(id=user_id).exists():
            contact = Contact.objects.filter(id=user_id).delete()
            return JsonResponse({
                "message": f"{contact.id},has been deleted",
            })
        else :
            return jsonResponse({
                "message":"user_id not exists in List"
            },status=400)
    else :
        return({
            "message":"invalied http request"
        },status=405)



