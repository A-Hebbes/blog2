from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.http import JsonResponse

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

def delete_comment(request, slug, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user: 
        comment.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'comment_id': comment_id})
        else:
            messages.add_message(request, messages.SUCCESS, 'Your Comment Has Been Deleted')
    else: 
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Comments Can Only Be Deleted By Their Creator'}, status=403)
        else:
            messages.add_message(request, messages.ERROR, 'Comments Can Only Be Deleted By Their Creator')

    return HttpResponseRedirect(reverse('post_full', args=[slug]))        

"""
FUNCTION PRIOR TO ATTEMPT TO FIX IT 
def delete_comment(request, slug, comment_id):
            queryset = Post.objects.filter(status=1)
            comment = get_object_or_404(Comment, pk=comment_id)

            if comment.author == request.user: 
                comment.delete()
                messages.add_message(request, messages.SUCCESS, 'Your Comment Has Been Delted')
            else: 
                messages.add_message(request, messages.ERROR, 'Comments Can Only Be Deleted By Their Creator')

            return HttpResponseRedirect(reverse('post_full', args=[slug]))
            
"""

            

"""

def edit_comment(request, slug, comment_id):
    if request.method == "POST" and request.is_ajax():
        comment = get_object_or_404(Comment, pk=comment_id)
        if comment.author == request.user:
            comment.body = request.POST.get('body', '')
            comment.save()
            return JsonResponse({'success': True, 'new_body': comment.body})
    return JsonResponse({'success': False}, status=400)
"""