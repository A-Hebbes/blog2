from django.urls import path
from .views import views

urlpatterns = [
    path('upcoming/', upcoming_view, name='upcoming_posts'),
]
