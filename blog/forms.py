from django import forms
from .models import Post, Comment, PostCd


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text',]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text',]

class PostCad(forms.ModelForm):

    class Meta:
        model = PostCd
        fields = ['nome', 'cidade', 'estado', 'idade', 'endereço', 'sexo', 'profissão']