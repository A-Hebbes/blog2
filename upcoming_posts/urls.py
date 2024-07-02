from . import views
from django.urls import path
#from .views import upcoming_view

urlpatterns = [
    path('upcoming/', upcoming_view, name='upcoming_posts'),
    #path('', views.upcoming_posts, name='upcoming'),
]
