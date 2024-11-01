from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('drafts/', views.draft_posts, name='draft_posts'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('<slug:slug>/', views.post_full, name='post_full'),
    path(
        '<slug:slug>/comment_edit/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment'
        ),
    path(
        'delete_comment/<slug:slug>/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment'
        ),

    path('tags/', views.tag_list, name='tag_list'),
    path('tag/<slug:slug>/', views.tag_detail, name='tag_detail'),
]