'''
author: jasonbanjui
date: '19-2-15 下午8:58'
'''
from . import models
import xadmin


class CommentAdmin(object):
    list_display = search_fields = list_filter = ['id', 'name', 'make_time']
    list_editable = ['name']
    ordering = ['-id']
    relfield_style = 'fk-ajax'
    refresh_tiems = [3, 5]
    readonly_fields = ['id']


xadmin.site.register(models.Comment, CommentAdmin)