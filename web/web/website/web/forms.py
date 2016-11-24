from django import forms
from .models import Post
from .models import Post1


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["content",]

class PostForm1(forms.ModelForm):
	class Meta:
		model = Post1
		fields = ["hash1","hash2","hash3",]