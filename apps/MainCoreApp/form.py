'''
author: jasonbanjui
date: '19-2-14 下午3:53'
'''
from django import forms
from . import models
from captcha.fields import CaptchaField


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = models.ArticleComment
        fields = ['com_username', 'com_content']
    captcha = CaptchaField()
