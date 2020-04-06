from django.db import models
from django.db.models import F


class CountModel(models.Model):
    name = models.CharField(verbose_name="Item Name", max_length=50, primary_key=True)
    num_count = models.BigIntegerField(verbose_name="Count Number")

    def __str__(self):
        return str(self.name)

    @classmethod
    def get_or_create_counter(cls, name):
        if not cls.objects.filter(name=name).exists():
            cls.objects.create(name=name, num_count=0)
        return cls.objects.filter(name=name).first().num_count

    @classmethod
    def increase_or_create_counter(cls, name):
        if cls.objects.filter(name=name).exists():
            cls.objects.filter(name=name).update(num_count=F("num_count")+1)
        else:
            cls.objects.create(name=name, num_count=1)
        return cls.objects.filter(name=name).first().num_count

    class Meta:
        verbose_name = verbose_name_plural = "Count Info"
        # 排序
        # ordering = ['-name']
        # 声明此元选项所属的 APP
        app_label = "echo_app"
        # 当前模型生成的表名，友情建议：使用MySQL数据库时，db_table用小写英文
        db_table = "count_info"
