from django.urls import path,include
from Admin import views
app_name="Admin"

urlpatterns = [
    path('district/',views.district,name="district"),
    path('deletedistrict/<int:did>',views.DeleteDistrict,name="DeleteDistrict"),
    path('EditDistrict/<int:did>',views.EditDistrict,name="EditDistrict"),
    path('brand/',views.brand,name="brand"),
    path('deletebrand/<int:did>',views.DeleteBrand,name="DeleteBrand"),
    path('category/',views.category,name="category"),
    path('deletecategory/<int:did>',views.DeleteCategory,name="DeleteCategory"),
    path('Home/',views.home,name="home"),
    path('Breed/',views.breed,name="breed"),
    path('delbreed/<int:id>',views.delbreed,name="delbreed"),
    path('place/',views.place,name="place"),
    path('deleteplace/<int:did>',views.DeletePlace,name="DeletePlace"),
    path('viewshop/',views.viewshop,name="viewshop"),
    path('acceptshop/<int:aid>',views.acceptshop,name="AcceptShop"),
    path('viewacceptedshop/',views.viewacceptedshop,name="viewacceptedshop"),
    path('rejectshop/<int:rid>',views.rejectshop,name="RejectShop"),
    path('viewrejectedshop/',views.viewrejectedshop,name="viewrejectedshop"),
    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('logout/',views.logout,name="logout"),
    path('reply/<int:id>',views.reply,name="reply"),
]