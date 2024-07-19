from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

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
    user_comments = post.comments.all().order_by("-created_on")
    total_comments = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit+False)
            comment.author = request.user
            comment.post = post
            comment.save()


    user = request.user
    comment_form = CommentForm()


    return render(
        request,
        "blog/post_full.html",
        {"post": post,
         "user_comments": user_comments,
         "total_comments": total_comments,
         "user": user,
         "comment_form": comment_form
        },
    )

def draft_posts(request):
    drafts = Post.objects.filter(status=0)  
    return render(request, 'blog/future_post.html', {'drafts': drafts})