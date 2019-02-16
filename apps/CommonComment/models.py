from django.db import models


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name=u"姓名",
                            null=False, blank=False)
    photo = models.ImageField(upload_to='comment/', verbose_name=u"头像",
                              default='coreuser/default/tx3.jpg', max_length=200,
                              null=False, blank=False)
    content = models.TextField(max_length=300, verbose_name=u"留言内容")
    make_time = models.DateField(auto_now_add=True, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"留言数据"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name