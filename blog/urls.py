from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('drafts/', views.draft_posts, name='draft_posts'),
    path('<slug:slug>/', views.post_full, name='post_full'),
    path('<slug:slug>/comment_edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
    
]