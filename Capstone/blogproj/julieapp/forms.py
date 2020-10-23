from django.forms import ModelForm
from blogapp.models import BlogPost

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude = []