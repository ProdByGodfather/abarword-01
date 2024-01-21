from django.shortcuts import render
from main.models import Post

def home(request):
    post = Post.objects.all().filter(best=True)
    context = {'posts':post}
    return render(request,'index.html',context)


def post(request,id):
    post = Post.objects.get(id=id)
    posts = Post.objects.all().filter(best=True).order_by("-create_time")[:4]
    context= {
        'post':post,
        'posts':posts,
    }
    return render(request,"single.html",context)


# def category(reqest,slug):

