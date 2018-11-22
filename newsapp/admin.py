from django.contrib import admin
# from newsapp.models import *
#
#
# # Register your models here.
#
#
#
#
# class TypeAdmin(admin.ModelAdmin):
#     # 在admin中显示水平
#     list_display = ["id", "name"]
#     # 给admin添加搜索功能
#     search_fields = ["id", "name"]
#     # 筛选字段
#     list_filter = ["id", "name"]
#     # 排序字段
#     ordering = ["id"]
#
#
# class UserInfoAdmin:
#     # 在admin中显⽰顺序
#     list_display = ["username", "gender", "mobile", "email", "is_staff", "is_superuser"]
#     # 给admin添加搜索功能
#     search_fields = ["username", "gender", "mobile", "email"]
#     # 筛选字段
#     list_filter = ["username", "gender", "mobile", "email"]
#     # 直接编辑字段
#     list_editable = ["is_staff", "is_superuser"]
#     # 排序字段
#     ordering = ["id"]
#
#
# class ContentAdmin:
#     # 在admin中显⽰顺序
#     list_display = ["id", "title", "picture"]
#     # 给admin添加搜索功能
#     search_fields = ["id", "publish_time", "title", "picture"]
#     # 排序字段
#     ordering = ["-publish_time"]
#
#
# class CommentAdmin:
#     # 在admin中显⽰顺序
#     list_display = ["id", "content", "user_id", "news_id","restore","restore_user"]
#     # 给admin添加搜索功能
#     search_fields = ["id", "publish_time", "user_id", "news_id"]
#     # 直接编辑字段
#     list_editable = ["restore","restore_user"]
#     # 排序字段
#     ordering = ["-publish_time"]
#
#
# admin.site.register(Type,TypeAdmin)
# admin.site.register(UserInfo,UserInfoAdmin)
# admin.site.register(Content,ContentAdmin)
# admin.site.register(Comment,CommentAdmin)
