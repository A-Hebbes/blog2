from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import UpcomingPost

# Create your views here.

#class UpcomingPostList(generic.ListView):
#    queryset = UpcomingPost.objects.filter(status=0)  
#    template_name = "upcoming_posts/upcoming.html" 

def upcoming_view(request):
    #upcoming_post = UpcomingPost.objects.all().order_by('-release_date').first()
    upcoming_posts = UpcomingPost.objects.filter(status=0).order_by('release_date')

    return render(
    request,
    "upcoming_posts/upcoming.html",
    {"upcoming_posts": upcoming_posts},
)

