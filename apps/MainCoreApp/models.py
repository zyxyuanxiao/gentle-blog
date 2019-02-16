from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class StromInfo(models.Model):
    photo = models.ImageField(upload_to='coreuser/image', verbose_name=u"头像", max_length=100,
                              default='article/default/default.jpg', null=True, blank=True)
    name = models.CharField(max_length=10, verbose_name=u"名字", null=False, blank=False, default=u'暂无')
    major = models.CharField(max_length=20, verbose_name=u"职业", null=False, blank=False, default=u'暂无')
    phone = models.CharField(max_length=18, verbose_name=u"电话", null=False, blank=False, default=u'暂无')
    email = models.EmailField(verbose_name=u"邮箱", default='xxx@qq.com', null=False, blank=False)
    wx = models.ImageField(upload_to='coreuser/image', verbose_name=u"微信", max_length=100,
                              default='coreuser/default/wx.jpg', null=True, blank=True)
    wxpay = models.ImageField(upload_to='coreuser/image', verbose_name=u"微信收款", max_length=100,
                              default='coreuser/default/wxzf.png', null=True, blank=True)
    zfbpay = models.ImageField(upload_to='coreuser/image', verbose_name=u"微信收款", max_length=100,
                              default='coreuser/default/zfbzf.jpg', null=True, blank=True)

    class Meta:
        verbose_name = u"站主信息"
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.name


class BlogBaseSet(models.Model):
    blog_name = models.CharField(max_length=10, verbose_name=u"博客头部名称",
                                 null=False, blank=False, default=u'我的个人博客')
    blog_foot_content = models.CharField(max_length=100, verbose_name=u"博客底部内容",
                                         null=False, blank=False, default=u'© 2017 Comply Theme. A Free Bootstrap 4 product landing page theme by Wired Dots.')

    class Meta:
        verbose_name = u"博客全局设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.blog_name


class ArticleType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=15, verbose_name=u"类型名称", null=False, blank=False)

    class Meta:
        verbose_name = u"文章类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name


class BlogNavSet(models.Model):
    nav_name = models.CharField(max_length=4, verbose_name=u"导航名", null=False,
                                blank=False, default=u'首页')
    nav_url = models.CharField(verbose_name=u"绑定 url", default='/', max_length=200)
    nav_articles_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE,
                                          verbose_name=u"绑定文章类型作为URL", null=True, blank=True)
    nav_sort = models.IntegerField(default=1, verbose_name=u"排序(数字越小越左)")

    class Meta:
        verbose_name = u"博客导航栏设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nav_name


class ArticleTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=10, verbose_name=u"标签名", null=False, blank=False)

    class Meta:
        verbose_name = u"文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class ArticlesMake(models.Model):
    id = models.AutoField(primary_key=True)
    cover = models.ImageField(upload_to='article/image', verbose_name=u"封面", max_length=100,
                              default='article/default/default.jpg', null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name=u"标题", null=False,
                             blank=False, default=u'暂无')
    introduction = models.TextField(max_length=300, verbose_name=u"简介", null=True, blank=True)
    content = RichTextUploadingField(verbose_name=u"内容")
    article_tags = models.ManyToManyField(ArticleTag, verbose_name=u"标签", null=True,
                                          blank=True, related_name='MainCoreApp_ArticlesMake_related')
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name=u"类型",
                                     null=True, blank=True, related_name='MainCoreApp_ArticlesMake_related')
    article_author = models.ForeignKey(StromInfo, on_delete=models.CASCADE, verbose_name=u"作者",
                                       related_name='MainCoreApp_ArticlesMake_related')
    like_num = models.IntegerField(default=0, verbose_name=u"喜欢数")
    read_num = models.IntegerField(default=0, verbose_name=u"阅读数")
    article_brief_time = models.DateField(auto_now_add=True, verbose_name=u"完成时间(简洁)")
    article_modify_time = models.DateTimeField(auto_now=True, verbose_name=u"更新时间")
    article_make_time = models.DateTimeField(auto_now_add=True, verbose_name=u"完成时间")
    is_recommend = models.BooleanField(default=False, verbose_name=u"是否推荐")
    is_top = models.BooleanField(default=False, verbose_name=u"是否置顶")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否在首页顶部")

    class Meta:
        verbose_name = u"编写文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class FriendshipLink(models.Model):
    id = models.AutoField(primary_key=True)
    link_name = models.CharField(max_length=25, verbose_name=u"链接名", null=False, blank=False)
    link_url = models.URLField(verbose_name=u"友链")

    class Meta:
        verbose_name = u"友情链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.link_name


class ArticleComment(models.Model):
    id = models.AutoField(primary_key=True)
    com_username = models.CharField(max_length=30, verbose_name=u"名字", null=False, blank=False)
    com_content = models.TextField(max_length=150, verbose_name=u"评论内容", null=False, blank=False)
    com_article = models.ForeignKey(ArticlesMake, on_delete=models.CASCADE, verbose_name=u"评论的文章", null=False,
                                       blank=False, related_name='MainCoreApp_ArticleCommend_relateds')
    com_make_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"文章评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.com_username