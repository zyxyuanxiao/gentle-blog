from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), {'title': '博客首页'}, name="index"),
    re_path('article/(?P<typeof>.*)/(?P<pid>.*)/', views.ArticleView.as_view(), name="article"),
    re_path('list/(?P<typeof>.*)/', views.ArticleView.as_view(), name="list"),
    path('comment/', views.AddArticleComment, name="Comment"),
    path('ThumbUp/', views.ThumbUp, name="ThumbUp"),
]
