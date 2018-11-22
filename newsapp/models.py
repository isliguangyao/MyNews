from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf.urls import include
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=6, verbose_name="新闻")

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "新闻类型"
        verbose_name_plural = verbose_name
        db_table = "new_type"


class UserInfo(AbstractUser):
    gender = models.CharField(max_length=1, choices=(("0", "男"), ("1", "女")), verbose_name="性别")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%y/%m", default="default.png", max_length=255, verbose_name="头像")

    def __str__(self):
        return "%s" % self.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        db_table = "user_info"


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to="UserInfo",
                                to_field="id",
                                related_name="context",
                                verbose_name="用户")
    type_id = models.ForeignKey(to="Type",
                                to_field="id",
                                related_name="context",
                                verbose_name="新闻类型")
    title = models.CharField(max_length=100,
                             verbose_name="标题")
    picture = models.CharField(max_length=20,
                               verbose_name="标签")
    content = RichTextUploadingField(verbose_name="新闻内容", null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",
                              default='default.png',
                              max_length=255,
                              verbose_name="文章图片")

    publish_time = models.DateTimeField(default=datetime.now,
                                        verbose_name="发布时间")
    clicked = models.IntegerField(verbose_name="点击量", default=0)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = "文章内容"
        verbose_name_plural = verbose_name
        db_table = "content"


class Comment(models.Model):
    id = models.AutoField(primary_key=Type)
    news_id = models.ForeignKey(to="Content", to_field="id", related_name="comment", verbose_name="评论文章")
    user_id = models.ForeignKey(to="UserInfo", to_field="id", related_name="comment", verbose_name="评论作者")
    content = models.TextField(verbose_name="评论内容")
    publish_time = models.DateTimeField(verbose_name="发布时间", default=datetime.now)
    # 4.5 回复:评论　评论
    restore = models.ForeignKey(to="self", to_field="id", verbose_name="回复对象", null=True, blank=True)
    restore_user = models.ForeignKey(to="UserInfo", to_field="id", related_name="restore", verbose_name="回复用户",
                                     null=True, blank=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "评论/回复"
        verbose_name_plural = verbose_name
        db_table = "news_comment"
