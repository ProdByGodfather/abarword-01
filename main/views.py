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


def category(reqest,slug):
    posts = Post.objects.all().filter(category__slug = slug)
    context = {
        'posts':posts,
        "category": slug
    }
    return render(reqest, "category.html", context)

def contact(reqest):
    context = {'message':None}
    if reqest.method == "POST":
        title = reqest.POST.get('title')
        email = reqest.POST.get('email')
        message = reqest.POST.get('message')
        print(title, email, message)
        Post.objects.create(title=title, email=email, message=message)
        context = {'message':"اطلاعات ذخیره شدند"}
    return render(reqest, 'contact.html',context)

