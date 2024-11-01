from django import forms
from .models import Comment, Post, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text='Separate tags with commas',
        widget=forms.TextInput(attrs={'placeholder': 'books, fiction, stories'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'status', 'tags']

    def clean_tags(self):
        if self.cleaned_data['tags']:
            return [tag.strip().lower() for tag in self.cleaned_data['tags'].split(',') if tag.strip()]
        return []

    def save(self, commit=True):
        post = super().save(commit=False)
        
        if commit:
            post.save()
            
            tag_names = self.clean_tags()
            post.tags.clear()
            
            for tag_name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)
                
        return post