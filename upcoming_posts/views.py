from django.shortcuts import render
from .models import UpcomingPost

# Create your views here.

def upcoming_view(request):
    upcoming_post = UpcomingPost.objects.all().order_by('-release_date').first()

return render(
    request,
    "upcoming_posts/upcoming.html",
    {"upcoming_posts": upcoming_posts},
)

