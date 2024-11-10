from django import forms
from .models import Comment, Post, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text='Separate tags with commas (e.g., books, fiction, stories)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter tags separated by commas'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            'excerpt': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            existing_tags = self.instance.tags.all()
            if existing_tags:
                self.initial['tags'] = ', '.join(
                    tag.name for tag in existing_tags
                )

    def clean_tags(self):
        tag_string = self.cleaned_data.get('tags')
        if isinstance(tag_string, list):
            tag_string = ', '.join(tag_string)
        tag_string = str(tag_string or '')
        return [
            tag.strip().lower()
            for tag in tag_string.split(',')
            if tag.strip()
            ]

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            tag_names = self.clean_tags()
            post.tags.clear()
            if tag_names:
                for tag_name in tag_names:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)
        return post
