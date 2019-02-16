from django.shortcuts import render, HttpResponse
from apps.MainCoreApp.models import StromInfo, BlogBaseSet, BlogNavSet
from django.views.generic.base import View
from . import models, forms
import json


class CommentView(View):
    def get(self, request):
        title = "留言"
        comments = models.Comment.objects.all()
        user = StromInfo.objects.all()[0]
        base = BlogBaseSet.objects.all()[0]
        nav = BlogNavSet.objects.all()
        return render(request, 'comment.html', locals())

    def post(self, request):
        if request.is_ajax():
            if request.method == 'POST':
                comment = forms.CommentForm(request.POST, request.FILES)
                if comment.is_valid():
                    comment.save()
                    comments = models.Comment.objects.all()
                    comment_all = {}
                    for index, item in enumerate(comments):
                        comment_all[index] = {
                            'name': item.name,
                            'img': str(item.photo),
                            'content': item.content
                        }
                    return HttpResponse(json.dumps(comment_all),
                                        content_type='application/json', status=200)
                return HttpResponse(json.dumps(comment.errors),
                                    content_type='application/json', status=500)