from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('drafts/', views.draft_posts, name='draft_posts'),
    path('<slug:slug>/', views.post_full, name='post_full'),
    
]