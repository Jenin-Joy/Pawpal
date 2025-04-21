from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [
   path('Login/',views.login,name="login"),
   path('Shop/',views.shop,name="shop"),
   path('Ajaxplace/',views.ajaxplace,name="ajaxplace"),
   path('Pet/',views.pet,name="pet"),
   path('Ajaxbreed/',views.ajaxbreed,name="ajaxbreed"),
   path('',views.index,name="index"),
   
]