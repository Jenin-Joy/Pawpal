from django.urls import path,include
from Pet import views

app_name="Pet"

urlpatterns = [
    path('Home/',views.home,name="home"),
    path('MyProfile/',views.myprofile,name="myprofile"),
    path('EditProfile/',views.editprofile,name="editprofile"),
    path('ChangePassword/',views.changepassword,name="changepassword"),
    path('AddPost/',views.addpost,name="addpost"),
    path('delpost/<int:did>',views.delpost,name="delpost"),
    path('viewpost/',views.viewpost,name="viewpost"),
    path('comment/<int:pid>',views.comment,name="comment"),
    path('delcomment/<int:cid>/<int:pid>',views.delcomment,name="delcomment"),
    path('like/<int:pid>',views.like,name="like"),
    path('group/',views.group,name="group"),
    path('deletegroup/<int:id>',views.deletegroup,name="deletegroup"),
    path('lostpet/',views.lostpet,name="lostpet"),
    path('viewgroup/',views.viewgroup,name="viewgroup"),
    path('viewlostpet/',views.viewlostpet,name="viewlostpet"),
    path('joingroup/<int:id>',views.joingrp,name="joingroup"),
    path('complaint/',views.complaint,name="complaint"),
    path('feedback/',views.feedback,name="feedback"),
    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('delcomplaint/<int:did>',views.delcomplaint,name="delcomplaint"),

    #chat
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('ajaxgetdata/',views.ajaxgetdata,name="ajaxgetdata"),
    path('viewuser/',views.viewuser,name="viewuser"),
    path('sendfriendrequest/',views.sendfriendrequest,name="sendfriendrequest"),
    path('notification/',views.notification,name="notification"),
    path('acceptrequest/',views.acceptrequest,name="acceptrequest"),

    path('ajaxsearchusers/',views.ajaxsearchusers,name="ajaxsearchusers"),

    path('like/',views.like,name="like"),
    path('getcomment/',views.getcomment,name="getcomment"),
    path('ajaxcomment/',views.ajaxcomment,name="ajaxcomment"),
    path('sharepost/',views.sharepost,name="sharepost"),
    path('viewmembers/<int:id>',views.viewmembers,name="viewmembers"),

    path('groupchatpage/<int:id>',views.groupchatpage,name="groupchatpage"),
    path('groupajaxchat/',views.groupajaxchat,name="groupajaxchat"),
    path('groupajaxchatview/',views.groupajaxchatview,name="groupajaxchatview"),

    path('logout/',views.logout,name="logout"),
    path('viewshops/',views.viewshops,name="viewshops"),
    path('viewproducts/<int:id>',views.viewproducts,name="viewproducts"),


    path('shopchatpage/<int:id>',views.shopchatpage,name="shopchatpage"),
    path('shopajaxchat/',views.shopajaxchat,name="shopajaxchat"),
    path('shopajaxchatview/',views.shopajaxchatview,name="shopajaxchatview"),
    path('shopclearchat/',views.shopclearchat,name="shopclearchat"),
]