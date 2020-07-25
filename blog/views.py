from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {'author':'Vikram Vikrant','title':'Blog-post 1','content':'First Post Content','date':'july 24,2020'},
    {'author':'Rahul Sharma','title':'Blog-post 2','content':'Second Post Content','date':'july 25,2020'},
]
# Create your views here.
def home(request):
    context={
        'posts':posts
    }

    return render(request,'blog/home.html',context)

def about(request):
        return render(request,'blog/about.html',{'title':'About Page'})