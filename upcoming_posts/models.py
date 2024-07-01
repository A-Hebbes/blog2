from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UpcomingPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="upcoming_posts")
    status = models.IntegerField(default=0)
    release_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title