from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='分类名', unique=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    desc = models.CharField(max_length=100, blank=True, verbose_name='描述')
    content = models.TextField(verbose_name='内容')
    markdown_content = models.TextField(verbose_name='markdown内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    view = models.IntegerField(default=0, verbose_name='查看次数')
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title
