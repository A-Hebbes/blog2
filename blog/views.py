from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

#class PostList(generic.ListView):
#    model = Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_full(request, slug):
    
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_full.html",
        {"post": post},
    )

def draft_posts(request):
    drafts = Post.objects.filter(status=0)  
    return render(request, 'blog/future_post.html', {'drafts': drafts})