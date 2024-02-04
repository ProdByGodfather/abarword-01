from django.shortcuts import render
from main.models import Post, Contact
# import messages in django contrib
from django.contrib import messages

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


def category(request,slug):
    posts = Post.objects.all().filter(category__slug = slug)
    context = {
        'posts':posts,
        "category": slug
    }
    return render(request, "category.html", context)

def contact(request):
    if request.method == "POST":
        title = request.POST.get('title')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(title, email, message)
        Contact.objects.create(title=title, email=email, message=message)
        messages.info(request, 'پیغام شما با موفقیت ذخیره شد.')
    return render(request, 'contact.html')

