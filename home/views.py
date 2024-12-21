from django.shortcuts import render, redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login as auth_login, authenticate


# Create your views here.

#this is known as url despatching
def index(req):                
    content = {                #content->variable. 
        "name" : "abhishek",
        "age" : 19,
        "learning" : "django which is a python framework"
    }
    # messages.success(req,'this is a success message')
    return render(req, 'index.html', content)
    # return HttpResponse("this is  home pge fucking yeh")
    
    
def about(req):
    return render(req, 'about.html',)
#    return HttpResponse("this is  bout pge fucking yeh")



def profile(req):
    return render(req, 'profile.html',)
    # return HttpResponse("this is  profile pge ")
    

def contact(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        desc = req.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        # return redirect('success')
        messages.success(req, 'Your data has been successfully submitted')
    
    
    return render(req, 'contact.html') 


def signup(req):
    if(req.method == 'POST'):
        firstname = req.POST.get('first-name')
        lastname = req.POST.get('last-name')
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = User.objects.filter(username=username)


        if user.exists():
            messages.info(req, 'username already taken!')
            return redirect('signup')

        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        
        messages.info(req, "Account created Successfully!")
        JsonResponse({'message' : 'user successfully stored to database'})
        return redirect('signup')
        
    return render(req, 'signup.html')  


def login(req):
    if(req.method == 'POST'):   
        username = req.POST.get('username')
        password = req.POST.get('password')
        
        print(f"Username from form: '{username}'and password : {password}")
        print('req.post : ',req.POST)


        if not User.objects.filter(username=username).exists():
            messages.error(req, "username doesn't exists")
            # return redirect('login')
        else : 
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(req, 'Invalid user credentials')
                return redirect('login')
            else:
                auth_login(req,user)
                return redirect('/')
            
            
    return render(req, 'login.html')  

  
def success(req):
    return render(req, 'success.html')

def change_password(req):
    if req.method =='POST':
        current_password = req.POST.get('current-password')
        new_password = req.POST.get('new-password')
        confirm_password = req.POST.get('confirm-password')
        
        if (new_password != confirm_password):
            messages.error(req, "new password and confirm password didn't match")

        user=req.user #returns the logged in user.
        print('user : ',user)
        #matching the current password and entered current_password
        if not user.check_password(new_password):
            messages.error(req, 'current password did not matched')
            
    return render(req, 'change_password.html')
  



def forgot_password(req):
    pass #TODO: sending emails for otp and do chatGpt for further things to do.

# for fetching images from unsplash api 
# def get_image_url(request):
#     client_id = "OxAl8FBKvdG8VQGe16QlNDredx2oLG-AceheNt4NDGw"
#     access_key = "zy42VYKWKKK4q1D2-wABtUeiwMSjiN8trBOP30KDGuE"
#     api_url = "https://api.unsplash.com/photos/?client_id=access_key/photos/random"

#     headers = {
#        "Authorization": f"{client_id} {access_key}"
#     }

#     response = requests.get(api_url, headers=headers)

#     if response.status_code == 200:
#         data = response.json()
#         print('data : ',data)
#         image_url = data.get("url") 
#         return JsonResponse({"url": image_url})
#     else:
#         return JsonResponse({"error": "Failed to fetch image"}, status=500)





