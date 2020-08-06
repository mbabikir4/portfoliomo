from django.shortcuts import render,get_object_or_404
from .models import Blag

# Create your views here.

Blags = Blag.objects.all()

def all_blogs(request):
    return render(request,'blog/all_blogs.html',{'Blags':Blags})

def detail(request,blog_id):
    blog = get_object_or_404(Blag,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})

