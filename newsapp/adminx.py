from newsapp.models import *
import xadmin
from xadmin import views


# Register your models here.
class Basesetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = "瞎扯蛋后台管理系统"
    site_footer = "瞎扯蛋新闻网"
    menu_style = "accordion"


class TypeAdmin:
    # 在admin中显示水平
    list_display = ["id", "name"]
    # 给admin添加搜索功能
    search_fields = ["id", "name"]
    # 筛选字段
    list_filter = ["id", "name"]
    # 排序字段
    ordering = ["id"]


class ContentAdmin:
    # 在admin中显⽰顺序
    list_display = ["id", "title", "picture"]
    # 给admin添加搜索功能
    search_fields = ["id", "publish_time", "title", "picture"]
    # 排序字段
    ordering = ["-publish_time"]
    list_per_page = 10


class CommentAdmin:
    # 在admin中显⽰顺序
    list_display = ["id", "content", "user_id", "news_id", "restore", "restore_user"]
    # 给admin添加搜索功能
    search_fields = ["id", "publish_time", "user_id", "news_id"]
    # 直接编辑字段
    list_editable = ["restore", "restore_user"]
    # 排序字段
    ordering = ["-publish_time"]


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, Basesetting)
xadmin.site.register(Type, TypeAdmin)
xadmin.site.register(Content, ContentAdmin)
xadmin.site.register(Comment, CommentAdmin)
