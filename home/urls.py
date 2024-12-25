from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path('',views.index, name='home'),
   # path('about',views.about, name='about'),
   path('profile',views.profile, name='profile'),
   path('contact',views.contact,name='contact'),
   # path('success',views.success,name='success'),
   path('signup',views.signup,name='signup'),
   path('login',views.login,name='login'),
   path('change_password/',views.change_password,name='change_password'),
   # path('get-image-url/', views.get_image_url, name='get_image_url'),
]