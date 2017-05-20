from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# 为每一个用户创建TOKEN
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# 文章信息类
class Content(models.Model):
    REC = 'REC'
    NOREC = 'NOREC'
    rec_choices = (
        (REC, 'REC'),
        (NOREC, 'NOREC'),
    )
    # 文章标题
    content_title = models.CharField(max_length=100)
    # 文章提纲
    outline = models.CharField(max_length=200)
    # 文章内容
    content_text = models.TextField(null=True, blank=True)
    # 观看数目
    view_num = models.IntegerField(default=0)
    # 收藏数量
    collect_num = models.IntegerField(default=0)
    # 文章分类id
    contenttypeid = models.IntegerField()
    # 文章id
    contentid = models.IntegerField(primary_key=True)
    # 文章作者
    author = models.CharField(max_length=50)
    # 发表时间
    date = models.DateTimeField()
    # 是否推荐标签，true为推荐
    recimfor = models.CharField(max_length=10, choices=rec_choices, default=NOREC)
    # 文章图片
    content_image = models.ImageField(upload_to='contentimage/', null=True, blank=True)

    def __str__(self):
        return self.content_title

# 标签信息类
class icons(models.Model):
    # 标签名字
    icon_name = models.CharField(max_length=20)
    # 分类id
    labelid = models.IntegerField()
    # 标签图标
    icon_image = models.ImageField(upload_to='iconimage/', null=True)

    def __str__(self):
        return self.icon_name

#用户收藏信息
class userprofile(models.Model):
    phone_num = models.CharField(max_length=30)
    wechat_openid = models.CharField(max_length=50)
    true_name = models.CharField(max_length=20)
    collect = models.TextField(null=True)

    def __str__(self):
        return self.true_name
