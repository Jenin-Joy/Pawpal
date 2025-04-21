from django.urls import path,include
from Shop import views
app_name="Shop"

urlpatterns = [
    path('Home/',views.home,name="home"),
    path('MyProfile/',views.myprofile,name="myprofile"),
    path('EditProfile/',views.editprofile,name="editprofile"),
    path('ChangePassword/',views.changepassword,name="changepassword"),
    path('AddProduct/',views.addproduct,name="addproduct"),
    path('delproduct/<int:did>/<int:status>',views.delproduct,name="delproduct"),
    path('logout/',views.logout,name="logout"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('ajaxgetdata/',views.ajaxgetdata,name="ajaxgetdata"),
]