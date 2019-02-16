from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.views.generic.base import View
from pure_pagination import Paginator
from django.utils.http import unquote
from . import form
import json


class IndexView(View):
    def get(self, request, title):
        try:
            base = models.BlogBaseSet.objects.all()[0]
            user = models.StromInfo.objects.all()[0]
            article = models.ArticlesMake.objects.order_by('-article_make_time')
            banner = models.ArticlesMake.objects.filter(is_banner=True).order_by('-like_num', '-read_num')[:3]
            recommend = models.ArticlesMake.objects.filter(is_recommend=True).order_by('-like_num', '-read_num')[:6]
            read = models.ArticlesMake.objects.order_by('-read_num')[:6]
            link = models.FriendshipLink.objects.all()[:3]
            nav = models.BlogNavSet.objects.all()
            title = title
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            pure = Paginator(article, 10, request=request)
            new = pure.page(page)
            return render(request, 'index.html', locals())
        except:
            return redirect('/xadmin/')


class ArticleView(View):
    def get(self, request, typeof, pid=''):
        if pid:
            # 获取文章
            typeof = unquote(typeof)
            article_list = models.ArticleType.objects.filter(type_name=typeof)[0].MainCoreApp_ArticlesMake_related.all()
            if article_list:
                pid = title = unquote(pid)
                article = models.ArticlesMake.objects.filter(title=pid)[0]
                base = models.BlogBaseSet.objects.all()[0]
                user = models.StromInfo.objects.all()[0]
                nav = models.BlogNavSet.objects.all()
                read = models.ArticlesMake.objects.order_by('-read_num')[:6]
                recommend = article_list.filter(is_recommend=True).all().order_by('-like_num', '-read_num')[:5]
                # 上下篇
                try:
                    up_page = article_list.get(id=article.id - 1)
                except:
                    up_page = False
                try:
                    down_page = article_list.get(id=article.id + 1)
                except:
                    down_page = False
                # 相关文章
                related_article = []
                for item in article.article_tags.all():
                    for i in item.MainCoreApp_ArticlesMake_related.all():
                        if i not in related_article:
                            related_article.append(i)
                related_article = related_article[:6]
                comment = form.ArticleCommentForm()
                try:
                    comment_all = article.MainCoreApp_ArticleCommend_relateds.all()
                except:
                    comment_all = False
                if article:
                    response = render(request, 'info.html', locals())
                    if str(article.id) not in request.COOKIES:
                        response.set_cookie(str(article.id), str(article.id), max_age=60*60*24)
                        article.read_num += 1
                        article.save()
                    return response
        else:
            # 文章列表
            title = typeof = unquote(typeof)
            is_search = False
            try:
                article_list = models.ArticleType.objects.filter(type_name=typeof)[0].MainCoreApp_ArticlesMake_related.all().order_by('-article_make_time')
                title = '文章类型： ' + title
            except:
                try:
                    article_list = models.ArticleTag.objects.filter(tag_name=typeof)[0].MainCoreApp_ArticlesMake_related.all().order_by('-article_make_time')
                    title = '文章标签： ' + title
                except:
                    title = '搜索： ' + title
                    is_search = True
                    article_list = []
                    article_all = models.ArticlesMake.objects.all()
                    for item in article_all:
                        is_filter = False
                        is_introduction = False
                        temp = {
                            'article_search': item
                        }
                        keyword = '<span style="background-color:yellow">' + typeof + '</span>'
                        if typeof in item.title:
                            item.title = item.title[:item.title.find(typeof)] + keyword + item.title[item.title.find(typeof) + len(typeof):]
                            is_filter = True
                        if typeof in item.introduction:
                            item.introduction = item.introduction[:item.introduction.find(typeof)] + keyword + item.introduction[item.title.find(typeof) + len(typeof):]
                            is_introduction = True
                            is_filter = True
                        if typeof in item.content:
                            item.content = item.content[item.content.find(typeof) + len(typeof):item.content.find(typeof) + len(typeof) + (len(typeof) * 100)]
                            is_filter = True
                        if is_filter:
                            temp['title'] = item.title
                            temp['introduction'] = item.introduction
                            temp['content'] = item.content
                            temp['is_introduction'] = is_introduction
                            temp['keyword'] = keyword
                            article_list.append(temp)
            base = models.BlogBaseSet.objects.all()[0]
            user = models.StromInfo.objects.all()[0]
            nav = models.BlogNavSet.objects.all()
            read = models.ArticlesMake.objects.order_by('-read_num')[:6]
            try:
                recommend = article_list.filter(is_recommend=True).all().order_by('-like_num', '-read_num')[:5]
            except:
                recommend = False
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            pure = Paginator(article_list, 10, request=request)
            new = pure.page(page)
            return render(request, 'list.html', locals())


def AddArticleComment(request):
    if request.is_ajax():
        if request.method == 'POST':
            comment = form.ArticleCommentForm(request.POST)
            if comment.is_valid():
                com_username = request.POST.get('com_username', '')
                com_content = request.POST.get('com_content', '')
                id = request.POST.get('pid', '')
                article = models.ArticlesMake.objects.get(id=id)
                models.ArticleComment.objects.create(com_username=com_username,
                                                     com_content=com_content, com_article=article)
                comment_for_this = article.MainCoreApp_ArticleCommend_relateds.all().order_by('com_make_time')
                comment_all = {}
                for index, item in enumerate(comment_for_this):
                    comment_all[index] = {
                        'com_username': item.com_username,
                        'com_content': item.com_content,
                        'com_make_time': item.com_make_time.strftime('%Y-%m-%d-%H-%M-%S')
                    }
                return HttpResponse(json.dumps(comment_all), content_type='application/json', status=200)
            else:
                return HttpResponse(json.dumps(comment.errors), content_type='application/json', status=500)


def ThumbUp(request):
    if request.is_ajax():
        if request.method == 'GET':
            id = request.GET.get('id', '')
            article = models.ArticlesMake.objects.get(id=id)
            if article is not None:
                if request.COOKIES.get('0'+str(article.id), False):
                    response = HttpResponse(json.dumps({'mg': '你已经点过赞啦', 'tp': str(article.like_num)}),
                                            content_type='application/json', status=200)
                else:
                    article.like_num += 1
                    article.save()
                    response = HttpResponse(json.dumps({'mg': '点赞成功', 'tp': str(article.like_num)}),
                                            content_type='application/json', status=200)
                    response.set_cookie('0'+str(article.id), str(article.id), max_age=60*60*24)
                return response