from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm, PostForm


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
                'Your Comment Has Been Submitted. '
                'Your comment will be published once approved by the admin.'
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error with your comment submission. '
                'Please try again.'
            )

    user = request.user
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_full.html",
        {
            "post": post,
            "user_comments": user_comments,
            "total_comments": total_comments,
            "user": user,
            "comment_form": comment_form
        },
    )


def draft_posts(request):
    drafts = Post.objects.filter(status=0)
    return render(request, 'blog/future_post.html', {'drafts': drafts})


@login_required
def add_post(request):
    """Add a new blog post"""
    if not request.user.is_superuser:
        messages.add_message(
            request,
            messages.ERROR,
            'Only superusers can add posts'
        )
        return HttpResponseRedirect(reverse('home'))

    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your Post Has Been Created'
            )
            return HttpResponseRedirect(reverse('post_full', args=[post.slug]))
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error creating your post. Please try again.'
            )
    else:
        post_form = PostForm()

    return render(
        request,
        "blog/add_post.html",
        {
            "post_form": post_form,
        },
    )

@login_required
def edit_post(request, slug):
    """Edit an existing blog post"""
    if not request.user.is_superuser:
        messages.add_message(request, messages.ERROR, 'Only superusers can edit posts')
        return HttpResponseRedirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    
    if request.method == "POST":
        print("POST data received:", request.POST)  # Debug print
        print("Current tags before update:", list(post.tags.all()))  # Debug print
        
        post_form = PostForm(data=request.POST, instance=post)
        if post_form.is_valid():
            print("Form is valid")  # Debug print
            print("Cleaned tags data:", post_form.cleaned_data.get('tags', ''))  # Debug print
            
            post = post_form.save()
            print("Tags after save:", list(post.tags.all()))  # Debug print
            
            messages.add_message(request, messages.SUCCESS, 'The Post Has Been Updated')
            return HttpResponseRedirect(reverse('post_full', args=[post.slug]))
        else:
            print("Form errors:", post_form.errors)  # Debug print
            messages.add_message(request, messages.ERROR, 'There Was An Error Updating This Post')
    else:
        post_form = PostForm(instance=post)
        print("Initial tags:", [tag.name for tag in post.tags.all()])  # Debug print

    return render(
        request,
        "blog/edit_post.html",
        {
            "post_form": post_form,
            "post": post,
        },
    )


@login_required
def delete_post(request, slug):
    """Delete a blog post"""
    if not request.user.is_superuser:
        messages.add_message(
            request,
            messages.ERROR,
            'Only superusers can delete posts'
        )
        return HttpResponseRedirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        'The Post Has Been Deleted'
    )
    return HttpResponseRedirect(reverse('home'))

@login_required
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
            messages.add_message(
                request,
                messages.SUCCESS,
                'The Comment Has Been Updated'
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There Was An Error Updating This Comment'
            )

        return HttpResponseRedirect(reverse('post_full', args=[slug]))

@login_required
def delete_comment(request, slug, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your Comment Has Been Deleted'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Comments Can Only Be Deleted By Authorised Accounts'
        )

    return HttpResponseRedirect(reverse('post_full', args=[slug]))


def tag_list(request):
    tags = Tag.objects.annotate(post_count=models.Count('posts'))
    return render(request, 'blog/tag_list.html', {'tags': tags})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag, status=1)
    return render(request, 'blog/tag_detail.html', {
        'tag': tag,
        'posts': posts
    })
