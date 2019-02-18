'''
author: jasonbanjui
date: '19-2-13 下午6:22'
'''
from . import models
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
    menu_style = 'accordion'


class GlobalSettings(object):
    site_title = "后台博客管理系统"
    site_footer = "后台博客管理系统"
    menu_style = "accordion"


class StromInfoAdmin(object):
    list_display = search_fields = list_filter = list_editable = ['name', 'major', 'phone', 'email']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]
    model_icon = 'fa fa-user'


class BlogBaseSetAdmin(object):
    list_display = search_fields = list_filter = list_editable =['blog_name', 'blog_foot_content']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]


class ArticleTypeAdmin(object):
    list_display = search_fields = list_filter = ['id', 'type_name']
    list_editable = ['type_name']
    ordering = ['-id']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]
    readonly_fields = ['id']


class BlogNavSetAdmin(object):
    list_display = search_fields = list_filter = list_editable = ['nav_name',
                                                                  'nav_url', 'nav_sort']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]


class ArticleTagAdmin(object):
    list_display = search_fields = list_filter = ['id', 'tag_name']
    list_editable = ['tag_name']
    ordering = ['-id']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]
    readonly_fields = ['id']


class ArticlesMakeAdmin(object):
    list_display = search_fields = list_filter = ['id', 'title', 'article_tags', 'like_num', 'read_num',
                                                 'article_type', 'article_brief_time', 'article_modify_time',
                                                 'is_recommend', 'is_top', 'is_banner']
    list_editable = ['id', 'title', 'article_tags',
                     'article_type', 'is_recommend', 'is_top',
                     'is_banner']
    ordering = ['-id']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]
    readonly_fields = ['id', 'article_brief_time', 'article_modify_time',
                       'article_make_time', 'like_num', 'read_num']


class FriendshipLinkAdmin(object):
    list_display = search_fields = list_filter = ['id', 'link_name', 'link_url']
    list_editable = ['link_name', 'link_url']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]
    readonly_fields = ['id']


class ArticleCommentAdmin(object):
    list_display = search_fields = list_filter = list_editable = ['com_username', 'com_content']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]


xadmin.site.register(models.StromInfo, StromInfoAdmin)
xadmin.site.register(models.BlogBaseSet, BlogBaseSetAdmin)
xadmin.site.register(models.BlogNavSet, BlogNavSetAdmin)
xadmin.site.register(models.ArticleType, ArticleTypeAdmin)
xadmin.site.register(models.ArticleTag, ArticleTagAdmin)
xadmin.site.register(models.ArticlesMake, ArticlesMakeAdmin)
xadmin.site.register(models.FriendshipLink, FriendshipLinkAdmin)
xadmin.site.register(models.ArticleComment, ArticleCommentAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)