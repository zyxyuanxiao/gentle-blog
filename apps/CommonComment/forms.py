'''
author: jasonbanjui
date: '19-2-15 下午9:05'
'''
from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'photo', 'content']