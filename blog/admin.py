from django.contrib import admin
from .models import Post, Comment, Tag
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class CustomPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    filter_horizontal = ('tags',)  


admin.site.register(Comment)
admin.site.register(Tag)
