from django.contrib import admin

from .models import CountModel


@admin.register(CountModel)
class CountInfoAdmin(admin.ModelAdmin):
    # 按指定的顺序，显示指定的字段
    list_display = ("name", "num_count",)
    # 指定修改的字段的显示，若下面禁止了修改的链接，所以此处定义无用
    fields = ("name", "num_count",)

    # action 按钮所在的位置
    actions_on_top = True
    actions_on_bottom = True
    # save 按钮所在的位置
    save_on_top = True
    # 空值所填充的内容
    empty_value_display = '-empty-'
    # # 右侧的过滤器
    # list_filter = ('name', )
    # # 搜索栏支持的内容
    # search_fields = ['name', ]
    # 链接修改页面的字段
    list_display_links = ("name", )
    list_max_show_all = 200
    # 每个页面显示的记录数
    list_per_page = 100
    # 设置排序方式
    ordering = ["-name"]
    # 控制是否在 admin 页面显示 "View site" 的链接
    view_on_site = False