from django.shortcuts import render,redirect
from Shop.models import *
from Guest.models import *
from Pet.models import *
from django.db.models import Q
from datetime import datetime
from django.http import JsonResponse

# Create your views here.
def home(request):
    contact = []
    chatdata = tbl_chat.objects.filter(Q(shop_from=request.session['sid']) | Q(shop_to=request.session['sid']))
    for i in chatdata:
        contact.append(i.user_from.id if i.user_from != None else i.user_to.id)
    contact = list(set(contact))
    contact = tbl_pet.objects.filter(id__in=contact).order_by('-id')
    product=tbl_product.objects.filter(shop=request.session['sid']).order_by('-id')
    data= tbl_shop.objects.get(id=request.session['sid'])
    if request.method=="POST":
        tbl_product.objects.create(product_name=request.POST.get('txt_name'),
                                   product_description=request.POST.get('txt_description'),
                                   product_photo=request.FILES.get('file_photo'),
                                   product_price=request.POST.get('txt_price'),
                                   shop=data)
        return redirect("Shop:home",)
    else:
        return render(request,'Shop/Home.html',{'data':data,'product':product,'contact':contact})
    
def myprofile(request):
    shop=tbl_shop.objects.get(id=request.session['sid'])
    return render(request,'Shop/MyProfile.html',{'shop':shop})
def editprofile(request):
    editshop=tbl_shop.objects.get(id=request.session['sid'])
    if request.method=="POST":
        editshop.shop_name=request.POST.get("txt_name")
        editshop.shop_email=request.POST.get("txt_email")
        editshop.shop_contact=request.POST.get("txt_contact")
        editshop.shop_address=request.POST.get("txt_address")
        editshop.save()
        return redirect("Shop:myprofile")
    else:
       return render(request,'Shop/EditProfile.html',{'shop':editshop})
def changepassword(request):
    editpass=tbl_shop.objects.get(id=request.session['sid'])
    if request.method=="POST":
        oldpassword=request.POST.get("txt_oldpass")
        newpassword=request.POST.get("txt_newpass")
        repassword=request.POST.get("txt_repass")
        if editpass.shop_password==oldpassword:
            if newpassword==repassword:
               editpass.shop_password=newpassword
               editpass.save()
               return redirect("Shop:myprofile")
        else:
            return render(request,"Shop/ChangePass.html")
    else:
        return render(request,"Shop/ChangePass.html",{'shop':editpass})

def addproduct(request):
    product=tbl_product.objects.all()
    if request.method=="POST":
        tbl_product.objects.create(product_name=request.POST.get('txt_name'),
                                   product_description=request.POST.get('txt_description'),
                                   product_photo=request.FILES.get('file_photo'),
                                   product_price=request.POST.get('txt_price'))
        return redirect("Shop:addproduct",)
    else:
        return render(request,'Shop/AddProduct.html',{'product':product})

def delproduct(request,did, status):
    tbl_product.objects.get(id=did).delete()
    if status == 1:
        return redirect('Shop:home')
    else:
        return redirect('Shop:addproduct')

# right side pannel ajax---------------------------------------------------------------------------------------------
def ajaxgetdata(request):
    data= tbl_shop.objects.get(id=request.session['sid'])
    profile = {
        "name":data.shop_name,
        "photo":data.shop_photo.url
    }
    contact = []
    chatdata = tbl_chat.objects.filter(Q(shop_from=request.session['sid']) | Q(shop_to=request.session['sid']))
    for i in chatdata:
        contact.append(i.user_from.id if i.user_from != None else i.user_to.id)
    contact = list(set(contact))
    contact = tbl_pet.objects.filter(id__in=contact).order_by('-id')
    users = list(contact.values())
    return JsonResponse({"profile":profile,"users":users,"myid":request.session["pid"]})

def logout(request):
    del request.session["sid"]
    return redirect('Guest:index')

def chatpage(request,id):
    user  = tbl_pet.objects.get(id=id)
    return render(request,"Shop/Chat.html",{"user":user})

def ajaxchat(request):
    from_shop = tbl_shop.objects.get(id=request.session["sid"])
    to_user = tbl_pet.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),shop_from=from_shop,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Shop/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_shop.objects.get(id=request.session["sid"])
    chat_data = tbl_chat.objects.filter((Q(shop_from=user) | Q(shop_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Shop/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(shop_from=request.session["sid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(shop_to=request.session["sid"]))).delete()
    return JsonResponse({"msg":"Chat Deleted Sucessfully...."})
