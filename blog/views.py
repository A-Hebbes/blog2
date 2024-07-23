from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your Comment Has Been Submitted.\nYour comment will be published once approved by the admin.'
            )
        else: 
            messages.add_message(
                request, 
                messages.ERROR,
                'There was an error with your comment submission. Please try again.'
    )



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

"""
This view works prior to modal!!

def edit_comment(request, slug, comment_id):
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'The Comment Has Been Updated')
        else:
            messages.add_message(request, messages.ERROR, 'There Was An Error Updating This Comment')
        
        return HttpResponseRedirect(reverse('post_full', args=[slug]))

"""

def edit_comment(request, slug, comment_id):
    if request.method == "POST" and request.is_ajax():
        comment = get_object_or_404(Comment, pk=comment_id)
        if comment.author == request.user:
            comment.body = request.POST.get('body', '')
            comment.save()
            return JsonResponse({'success': True, 'new_body': comment.body})
    return JsonResponse({'success': False}, status=400)
