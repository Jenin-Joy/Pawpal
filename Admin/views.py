from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Pet.models import *

# Create your views here.
def district(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    data=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("txt_dstrct"))
        return redirect("Admin:district")
    else:
        return render(request,'Admin/District.html',{"District":data})

def DeleteDistrict(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:district")

def EditDistrict(request, did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    dis = tbl_district.objects.get(id=did)
    if request.method == "POST":
        dis.district_name = request.POST.get("txt_dstrct")
        dis.save()
        return redirect("Admin:district")
    return render(request,'Admin/District.html',{"dis":dis})

def brand(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    data=tbl_brand.objects.all()
    if request.method=="POST":
        tbl_brand.objects.create(brand_name=request.POST.get("txt_brand"))
        return redirect("Admin:brand")
    else:
        return render(request,'Admin/Brand.html',{"Brand":data})

def DeleteBrand(request,did):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    tbl_brand.objects.get(id=did).delete()
    return redirect("Admin:brand")

def category(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    data=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get("txt_cat"))
        return redirect("Admin:category")
    else:
        return render(request,'Admin/Category.html',{"Category":data})

def DeleteCategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("Admin:category")
def home(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    shop=tbl_shop.objects.filter(shop_status=1)
    data=tbl_admin.objects.get(id=request.session['aid'])
    return render(request,'Admin/Home.html',{'data':data,'shop':shop})

def breed(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    cat=tbl_category.objects.all()
    br=tbl_breed.objects.all()
    if request.method=='POST':
        breed=request.POST.get('txt_breed')
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_breed.objects.create(breed_name=breed,category=category)
        return redirect('Admin:breed')
    else:
        return render(request,'Admin/Breed.html',{'cat':cat,'br':br})

def delbreed(request,id):
    tbl_breed.objects.get(id=id).delete()
    return redirect('Admin:breed')

def place(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        tbl_place.objects.create(place_name=request.POST.get("txt_place"),district=tbl_district.objects.get(id=request.POST.get("sel_district")))
        return redirect("Admin:place")
    else:
        return render(request,'Admin/Place.html',{"district":district,"Place":data})

def DeletePlace(request,did):

    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:place")

def viewshop(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    shop=tbl_shop.objects.filter(shop_status=0)
    return render(request,'Admin/ViewShops.html',{'shop':shop})

def acceptshop(request,aid):
    shop=tbl_shop.objects.get(id=aid)
    shop.shop_status=1
    shop.save()
    return render(request,'Admin/ViewShops.html')

def viewacceptedshop(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    shop=tbl_shop.objects.filter(shop_status=1)
    return render(request,'Admin/AcceptShops.html',{'acceptshop':shop})

def rejectshop(request,rid):
    shop=tbl_shop.objects.get(id=rid)
    shop.shop_status=2
    shop.save()
    return render(request,'Admin/ViewShops.html')

def viewrejectedshop(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    shop=tbl_shop.objects.filter(shop_status=2)
    return render(request,'Admin/RejectShops.html',{'rejectshop':shop})

def reply(request,id):
    reply=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        reply.reply=request.POST.get('txt_reply')
        reply.complaint_status=1
        reply.save()
        return redirect("Admin:reply",id)
    else:
        return render(request,'Admin/Reply.html')

def viewcomplaint(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    complaint=tbl_complaint.objects.all()
    return render(request,'Admin/ViewComplaint.html',{'complaint':complaint})

def logout(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    del request.session["aid"]
    return redirect('Guest:index')