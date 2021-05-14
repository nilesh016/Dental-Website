from .models import Appointment,Reply
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings as conf_settings
from django.contrib.auth.models import User
from django.contrib import auth

from django.views import View

def home(request):
    if request.method=='POST':
        
        your_name=request.POST["your-name"]
        your_phone=request.POST["your-phone"]
        your_email=request.POST["your-email"]
        your_address=request.POST["your-address"]
        your_schedule=request.POST["your-scheldule"]
        your_date=request.POST["your-date"]
        your_message=request.POST["your-message"]
        if request.user.is_authenticated:
            Appointment.objects.create(name=your_name,phone=your_phone,email=your_email,address=your_address,schedule=your_schedule,message=your_message,date=your_date)
            messages.success(request,'APPOINTMENT SAVED')
        else:
            messages.error(request,'YOU SHOULD BE LOGGED IN')
            return redirect('login')

    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')
        
def service(request):
    return render(request, 'website/service.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def blog(request):
    return render(request, 'website/blog.html')

def blog_details(request):
    if request.method == 'POST':
        name = request.POST['message_name']
        email = request.POST['message_email']
        message = request.POST['message']
        Reply.objects.create(name=name,message=message,email=email)
        
        #send email to default address
        send_mail(
            'Follow up required for - ' + name,
            message,
            email,
            [conf_settings.CONTACT_US_FORM_EMAIL_TO],
            fail_silently=False,
        )

        messages.success(request, f' {message} SAVED')
        return redirect('blog_details')
    else:
        return render(request, 'website/blog_details.html')


        

     

      


    

def dentistry(request):
    return render(request, 'website/dentistry.html')


class login(View):

    def get(self,request):
        return render(request,'website/login.html')

    def post(self,request):
        print("method called")
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        context = {
            "username":username,
        }

        if username == '':
            messages.error(request,"Please Enter username")
            return render(request,'website/login.html',context=context)

        if password == '':
            messages.error(request,"Please Enter Password")
            return render(request,'website/login.html',context=context)

        if username and password:
            print("present")
            user = auth.authenticate(username=username,password=password)

            if user:
                if not user.is_active:
                    messages.error(request,'Please Activate Account.')
                    print("na")
                    return render(request,'webiste/login.html')
                elif user.is_active:
                    auth.login(request,user)
                    messages.success(request,"Welcome, "+ user.username + ". You are now logged in.")
                    print("success")
                    return redirect('home')
            else:
                messages.error(request,'Invalid credentials')
                print("invalid")
                return render(request,'website/login.html',context=context)
        else:
            messages.error(request,'Something went wrong.')
            print("some")
            return render(request,'website/login.html',context=context)



def register(request):
    if request.method=='GET':
       return render(request, 'website/register.html') 
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        username=request.POST['username']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                print('Email Already Registered')
            
            else:
                user=User.objects.create_user(email=email,first_name=first_name,last_name=last_name,username=username)
                user.set_password(password1)
                user.is_active = True
                user.save()
                
                print('User Created')
                return redirect('login')
        else:
            print('Password Not Matching!')
    
        return render(request, 'website/register.html')

class Logout(View):
	def get(self,request):
		auth.logout(request)
		messages.success(request,'Logged Out')
		return redirect('login')

        
def contact(request):
    if request.method == 'POST':
        name = request.POST['message_name']
        email = request.POST['message_email']
        message = request.POST['message']
        
        #send email to default address
        send_mail(
            'Follow up required for - ' + name,
            message,
            email,
            [conf_settings.CONTACT_US_FORM_EMAIL_TO],
            fail_silently=False,
        )

        messages.success(request, f'Hi {name}, Thanks for contacting us. We will follow up with you within next few business days.')
        return redirect('contact')
    else:
        return render(request, 'website/contact.html')


