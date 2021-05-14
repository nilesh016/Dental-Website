from django.urls import path
from .views import home,about,service,pricing,blog,blog_details,contact,dentistry,login,register,Logout

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('service', service, name='service'),
    path('pricing', pricing, name='pricing'),
    path('blog', blog, name='blog'),
    path('blogdetails', blog_details, name='blog_details'),
    path('contact', contact, name='contact'),
    path('dentistry', dentistry, name='dentistry'),
    
    path('login', login.as_view(), name='login'),
    path('register', register,name='register'),
    path('logout', Logout.as_view(),name='logout'),
]