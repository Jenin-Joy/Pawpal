from django.shortcuts import render,redirect
from Pet.models import *
from Guest.models import *
from Shop.models import *
from django.db.models import Q
from datetime import datetime
from django.http import JsonResponse

# Create your views here.
def home(request):
    post=tbl_post.objects.all().order_by('-id')
    for i in post:
        i.post_count = tbl_like.objects.filter(post=i.id).count()
        i.comment_count = tbl_comment.objects.filter(post=i.id).count()
        i.like_status = tbl_like.objects.filter(post=i.id,pet=request.session["pid"]).count()
    contact = tbl_friends.objects.filter(Q(from_user=request.session["pid"]) | Q(to_user=request.session["pid"]),status=1)
    data= tbl_pet.objects.get(id=request.session['pid'])

    shops = []
    chatdata = tbl_chat.objects.filter(Q(user_from=request.session['pid']) | Q(user_to=request.session['pid']))
    for i in chatdata:
        shops.append(i.shop_from.id if i.shop_from != None else i.shop_to.id)
    shops = list(set(shops))
    shops = tbl_shop.objects.filter(id__in=shops).order_by('-id')
    if request.method=="POST":
        tbl_post.objects.create(post_photo=request.FILES.get('file_photo'),
                                post_description=request.POST.get('txt_description'),
                                pet=tbl_pet.objects.get(id=request.session['pid']))
        return redirect("Pet:home")
    return render(request,'Pet/Home.html',{'contact':contact,'post':post,'data':data,'shops':shops})

def myprofile(request):
    pet=tbl_pet.objects.get(id=request.session['pid'])
    return render(request,'Pet/MyProfile.html',{'pet':pet})
def editprofile(request):
    editpet=tbl_pet.objects.get(id=request.session['pid'])
    print(editpet)
    if request.method=="POST":
        editpet.pet_name=request.POST.get("txt_name")
        editpet.pet_email=request.POST.get("txt_email")
        editpet.pet_bio=request.POST.get("txt_bio")
        editpet.save()
        return redirect("Pet:myprofile")
    else:
       return render(request,'Pet/EditProfile.html',{'pet':editpet})
def changepassword(request):
    editpass=tbl_pet.objects.get(id=request.session['pid'])
    if request.method=="POST":
        oldpassword=request.POST.get("txt_oldpass")
        newpassword=request.POST.get("txt_newpass")
        repassword=request.POST.get("txt_repass")
        if editpass.pet_password==oldpassword:
            if newpassword==repassword:
               editpass.pet_password=newpassword
               editpass.save()
               return redirect("Pet:myprofile")
        else:
            return render(request,"Pet/ChangePass.html")
    else:
        return render(request,"Pet/ChangePass.html",{'pet':editpass})
def addpost(request):
    pet=tbl_pet.objects.get(id=request.session['pid'])
    post=tbl_post.objects.filter(pet=pet)
    if request.method=="POST":
        tbl_post.objects.create(post_photo=request.FILES.get('file_photo'),
                                post_description=request.POST.get('txt_description'),
                                pet=pet)
        return redirect("Pet:addpost")
    else:
        return render(request,'Pet/AddPost.html',{"post":post})

def delpost(request,did):
    tbl_post.objects.get(id=did).delete()
    return redirect('Pet:addpost')
def viewpost(request):
    pet=tbl_pet.objects.get(id=request.session['pid'])
    post=tbl_post.objects.all()
    return render(request,'Pet/ViewPost.html',{'post':post,'pet':pet})
def comment(request,pid):
    post=tbl_post.objects.get(id=pid)
    data=tbl_comment.objects.all()
    if request.method=="POST":
        tbl_comment.objects.create(
                                   post_comment=request.POST.get('txt_comment'),
                                  post=post)
        return redirect("Pet:comment",pid)
    else:
        return render(request,'Pet/Comment.html',{"comment":data})
def delcomment(request,cid,pid):
    tbl_comment.objects.get(id=cid).delete()
    return redirect('Pet:comment',pid)
def like(request,pid):
    post=tbl_post.objects.get(id=pid)
    pet=tbl_pet.objects.get(id=request.session['pid'])
    shop=tbl_shop.objects.get(id=request.session['sid'])
    tbl_like.objects.create(pet=pet,
                                  post=post,
                                  shop=shop)
    
    return redirect('Pet:viewpost')
def group(request):
    group=tbl_grp.objects.all()
    if request.method=="POST":
        tbl_grp.objects.create(group_name=request.POST.get('txt_name'),
                            group_description=request.POST.get('txt_description'),
                            group_photo=request.FILES.get('file_photo'),
                            pet=tbl_pet.objects.get(id=request.session['pid']))
        return redirect('Pet:group')
    else:                        
        return render(request,'Pet/Group.html',{'pet':group})
def lostpet(request):
    lostpet=tbl_lostpet.objects.all()
    if request.method=="POST":
        tbl_lostpet.objects.create(lostpet_name=request.POST.get('txt_name'),
                            lostpet_description=request.POST.get('txt_description'),
                            lostpet_photo=request.FILES.get('file_photo'),
                            pet=tbl_pet.objects.get(id=request.session['pid']))
        return redirect('Pet:lostpet')
    else:                        
        return render(request,'Pet/LostPet.html',{'lostpet':lostpet})
def viewgroup(request):
    group=tbl_grp.objects.filter().exclude(pet=request.session["pid"])
    for i in group:
        i.member_count = tbl_grpmembers.objects.filter(group=i.id,pet=request.session["pid"]).count()
    return render(request,'Pet/ViewGroup.html',{'group':group,"petid":request.session['pid']})
    
def viewlostpet(request):
    lostpet=tbl_lostpet.objects.all()
    return render(request,'Pet/ViewLostpet.html',{'lostpet':lostpet})

def joingrp(request,id):
    pet=tbl_pet.objects.get(id=request.session['pid'])
    groupid=tbl_grp.objects.get(id=id)
    tbl_grpmembers.objects.create(pet=pet,group=groupid)
    return redirect('Pet:viewgroup')
def complaint(request):
    pet=tbl_pet.objects.get(id=request.session['pid'])
    complaint=tbl_complaint.objects.all()
    if request.method=="POST":
        tbl_complaint.objects.create(complaint_title=request.POST.get('txt_title'),
                                complaint_content=request.POST.get('txt_content'),
                                pet=pet)
        return redirect("Pet:complaint")
    else:
        return render(request,'Pet/Complaint.html',{'complaint':complaint})
def feedback(request):
    feedback=tbl_feedback.objects.all()
    if request.method=="POST":
        tbl_feedback.objects.create(feedback_content=request.POST.get('txt_content'))
        return redirect("Pet:feedback")
    else:
        return render(request,'Pet/Feedback.html',{'feedback':feedback})
def viewcomplaint(request):
    complaint=tbl_complaint.objects.all()
    return render(request,'Pet/ViewComplaint.html',{'complaint':complaint})
def viewfeedback(request):
    feedback=tbl_feedback.objects.all()
    return render(request,'Pet/ViewFeedback.html',{'feedback':feedback})
def delcomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect('Pet:complaint')

#chat

def chatpage(request,id):
    user  = tbl_pet.objects.get(id=id)
    return render(request,"Pet/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_pet.objects.get(id=request.session["pid"])
    to_user = tbl_pet.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Pet/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_pet.objects.get(id=request.session["pid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Pet/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["pid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(user_to=request.session["pid"]))).delete()
    return JsonResponse({"msg":"Chat Deleted Sucessfully...."})

def ajaxgetdata(request):
    data= tbl_pet.objects.get(id=request.session['pid'])
    contacts= tbl_friends.objects.filter(Q(from_user=request.session["pid"]) | Q(to_user=request.session["pid"]),status=1)
    profile = {
        "name":data.pet_name,
        "photo":data.pet_photo.url
    }
    users = []
    for contact in contacts:
        users.append({
            "from_user": {
                "id": contact.from_user.id,
                "pet_name": contact.from_user.pet_name,
                "pet_photo": contact.from_user.pet_photo.url
            },
            "to_user": {
                "id": contact.to_user.id,
                "pet_name": contact.to_user.pet_name,
                "pet_photo": contact.to_user.pet_photo.url
            }
        })

    shops = []
    chatdata = tbl_chat.objects.filter(Q(user_from=request.session['pid']) | Q(user_to=request.session['pid']))
    for i in chatdata:
        shops.append(i.shop_from.id if i.shop_from != None else i.shop_to.id)
    shops = list(set(shops))
    shops = tbl_shop.objects.filter(id__in=shops).order_by('-id')
    shs = list(shops.values())
    # users = list(contact.values())
    return JsonResponse({"profile":profile,"users":users,"myid":request.session["pid"],"shops":shs})

# def viewuser(request):
#     user = tbl_pet.objects.filter().exclude(id=request.session["pid"])
#     return render(request,"Pet/ViewUsers.html",{"user":user})

def viewuser(request):
    if 'pid' not in request.session:
        return redirect("Guest:login")
    
    # Get all users except the current user
    users = tbl_pet.objects.exclude(id=request.session["pid"])
    current_user_id = request.session["pid"]
    
    # Process each user to determine friend status
    for user in users:
        # Check if there's a friend relationship
        friend = tbl_friends.objects.filter(
            (Q(from_user_id=current_user_id, to_user_id=user.id) |
             Q(from_user_id=user.id, to_user_id=current_user_id))
        ).first()
        
        if friend:
            if friend.status == 1:
                user.friend_status = "friends"  # Status 1 means friends
            elif friend.to_user_id == current_user_id:
                user.friend_status = "accept"  # Current user received a request
                user.friend_id = friend.id  # Store friend ID for accept action
            elif friend.from_user_id == current_user_id:
                user.friend_status = "sent"  # Current user sent a request
        else:
            user.friend_status = "send_request"  # No relationship exists
    
    return render(request, "Pet/ViewUsers.html", {
        "user": users,
        "userid": current_user_id
    })

def sendfriendrequest(request):
    tbl_friends.objects.create(
        from_user = tbl_pet.objects.get(id=request.session["pid"]),
        to_user = tbl_pet.objects.get(id=request.GET.get("id"))
    )
    return JsonResponse({"msg":"Request Send Sucessfully"})

def notification(request):
    user = tbl_friends.objects.filter(to_user=request.session["pid"])
    return render(request,"Pet/Notification.html",{"user":user})

def acceptrequest(request):
    fr = tbl_friends.objects.get(id=request.GET.get("id"))
    fr.status = 1
    fr.save()
    return JsonResponse({"msg":"Request Accepted.."})

def ajaxsearchusers(request):
    user = tbl_pet.objects.filter(pet_name__istartswith=request.GET.get("name")).exclude(id=request.session["pid"])
    users = []
    for i in user:
        users.append({
            "pet_name":i.pet_name,
            "pet_photo":i.pet_photo.url,
            "id":i.id,
            "to_user":list(tbl_friends.objects.filter(to_user=i.id).values()),
            "from_user":list(tbl_friends.objects.filter(from_user=i.id).values())
        })
    return JsonResponse({"user":users})

def like(request):
    post=tbl_post.objects.get(id=request.GET.get("commentId"))
    pet=tbl_pet.objects.get(id=request.session['pid'])
    count = tbl_like.objects.filter(pet=pet,post=post).count()
    if count > 0:
        tbl_like.objects.get(pet=pet,post=post).delete()
        status = 0
    else:
        tbl_like.objects.create(pet=pet,post=post)
        status = 1
    like = tbl_like.objects.filter(post=request.GET.get("commentId")).count()
    return JsonResponse({"status":status,"likecount":like})

def getcomment(request):
    comment = tbl_comment.objects.filter(post=request.GET.get("pid"))
    comments = []
    for i in comment:
        comments.append({
            "comment":i.post_comment,
            "comment_date":i.comment_date,
            "pet_name":i.pet.pet_name,
            "pet_photo":i.pet.pet_photo.url
        })
    return JsonResponse({"comment":comments})

def ajaxcomment(request):
    tbl_comment.objects.create(
        post_comment = request.GET.get("comment"),
        post = tbl_post.objects.get(id=request.GET.get("pid")),
        pet = tbl_pet.objects.get(id=request.session["pid"]),
        comment_date = datetime.now()
    )
    comment = tbl_comment.objects.filter(post=request.GET.get("pid"))
    commentcount = tbl_comment.objects.filter(post=request.GET.get("pid")).count()
    comments = []
    for i in comment:
        comments.append({
            "comment":i.post_comment,
            "comment_date":i.comment_date,
            "pet_name":i.pet.pet_name,
            "pet_photo":i.pet.pet_photo.url
        })
    return JsonResponse({"comment":comments,"commentcount":commentcount})

def sharepost(request):
    tbl_chat.objects.create(chat_time=datetime.now(),user_from=tbl_pet.objects.get(id=request.session["pid"]),user_to=tbl_pet.objects.get(id=request.GET.get("contactId")),post=tbl_post.objects.get(id=request.GET.get("postId")))
    return JsonResponse({"msg":"Post Shared Sucessfully"})

def deletegroup(request, id):
    tbl_grp.objects.get(id=id).delete()
    return redirect('Pet:group')

def viewmembers(request, id):
    group = tbl_grp.objects.get(id=id)
    members = tbl_grpmembers.objects.filter(group=group)
    return render(request, 'Pet/ViewMembers.html', {'members': members, 'group': group})

def groupchatpage(request,id):
    user  = tbl_grp.objects.get(id=id)
    return render(request,"Pet/GroupChat.html",{"user":user})

def groupajaxchat(request):
    from_user = tbl_pet.objects.get(id=request.session["pid"])
    group = tbl_grp.objects.get(id=request.POST.get("tid"))
    tbl_groupchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,group=group,chat_file=request.FILES.get("file"))
    return render(request,"Pet/GroupChat.html")

def groupajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_pet.objects.get(id=request.session["pid"])
    chat_data = tbl_groupchat.objects.filter(group=tid).order_by('chat_time')
    return render(request,"Pet/GroupChatView.html",{"data":chat_data,"tid":user.id})

def logout(request):
    del request.session["pid"]
    return redirect('Guest:index')

def viewshops(request):
    shop=tbl_shop.objects.filter(shop_status=1)
    return render(request,'Pet/ViewShops.html',{"shop":shop})

def viewproducts(request,id):
    product=tbl_product.objects.filter(shop=id)
    return render(request,'Pet/ViewProducts.html',{"product":product})

def shopchatpage(request,id):
    user  = tbl_shop.objects.get(id=id)
    return render(request,"Pet/ShopChat.html",{"user":user})

def shopajaxchat(request):
    from_user = tbl_pet.objects.get(id=request.session["pid"])
    to_shop = tbl_shop.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,shop_to=to_shop,chat_file=request.FILES.get("file"))
    return render(request,"Pet/ShopChat.html")

def shopajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_pet.objects.get(id=request.session["pid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(shop_from=tid) | Q(shop_to=tid))).order_by('chat_time')
    return render(request,"Pet/ShopChatView.html",{"data":chat_data,"tid":int(tid)})

def shopclearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["pid"]) & Q(shop_to=request.GET.get("tid")) | (Q(shop_from=request.GET.get("tid")) & Q(user_to=request.session["pid"]))).delete()
    return JsonResponse({"msg":"Chat Deleted Sucessfully...."})