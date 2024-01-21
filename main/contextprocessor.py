from main.models import New, Post



def base(request):
    new = New.objects.all().order_by('-create_time')
    return {"news":new}

def best_post_2(request):
    posts = Post.objects.all().filter(best=True).order_by("-create_time")[:2]
    return {"posts_best":post}