from main.models import New, Post, Category



def base(request):
    new = New.objects.all().order_by('-create_time')
    return {"news":new}

def best_post_2(request):
    posts = Post.objects.all().filter(best=True).order_by("-create_time")[:2]
    return {"posts_best":posts}

def category_show(reqest):
    categories = Category.objects.all()
    return {'category_show':categories}