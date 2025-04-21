from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Pet.models import *

# Create your views here.
def login(request):
    if request.method=='POST':
        admincount=tbl_admin.objects.filter(admin_email=request.POST.get('txt_email'),admin_password=request.POST.get('txt_password')).count()
        shopcount=tbl_shop.objects.filter(shop_email=request.POST.get('txt_email'),shop_password=request.POST.get('txt_password')).count()
        petcount=tbl_pet.objects.filter(pet_email=request.POST.get('txt_email'),pet_password=request.POST.get('txt_password')).count()
        if admincount > 0:
            admin=tbl_admin.objects.get(admin_email=request.POST.get('txt_email'),admin_password=request.POST.get('txt_password'))
            request.session['aid']=admin.id
            return redirect('Admin:home')
        if shopcount > 0:
            shop=tbl_shop.objects.get(shop_email=request.POST.get('txt_email'),shop_password=request.POST.get('txt_password'))
            request.session['sid']=shop.id
            return redirect('Shop:home')
        if petcount > 0:
            pet=tbl_pet.objects.get(pet_email=request.POST.get('txt_email'),pet_password=request.POST.get('txt_password'))
            request.session['pid']=pet.id
            return redirect('Pet:home')
        else:
            return render(request,'Guest/Login.html',{'msg':'invalid'})
    else:
        return render(request,'Guest/Login.html')
def shop(request):
    dis =tbl_district.objects.all()
    if request.method=='POST':
        place=tbl_place.objects.get(id=request.POST.get('sel_place'))
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("file_photo")
        proof=request.FILES.get("file_proof")
        password=request.POST.get("txt_password")
        tbl_shop.objects.create(shop_name=name,
                               shop_email=email,
                               shop_contact=contact,
                               shop_address=address,
                               shop_photo=photo,
                               shop_proof=proof,
                               shop_password=password,
                               place=place)
        return redirect("Guest:shop")
    else:
        return render(request,'Guest/Shop.html',{'dis':dis}) 

def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render (request,'Guest/Ajaxplace.html',{'place':place})
def pet(request):
    cat=tbl_category.objects.all()
    if request.method=='POST':
        breed=tbl_breed.objects.get(id=request.POST.get("sel_breed"))
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        photo=request.FILES.get("file_photo")
        dob=request.POST.get("txt_dob")
        bio=request.POST.get("txt_bio")
        password=request.POST.get("txt_password")
        tbl_pet.objects.create(pet_name=name,
                               pet_email=email,
                               pet_photo=photo,
                               pet_dob=dob,
                               pet_bio=bio,
                               pet_password=password,
                               breed=breed)
        return redirect("Guest:pet")
    else:
        return render(request,'Guest/Pet.html',{'category':cat})
def ajaxbreed(request):
    breed=tbl_breed.objects.filter(category=request.GET.get("did"))
    return render (request,'Guest/Ajaxbreed.html',{'breed':breed})

def index(request):
    data = tbl_post.objects.all().order_by('-id')[:5]
    return render (request,'Guest/index.html',{'data':data})

