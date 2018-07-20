from django.db import models
from django.conf import settings
from articles.models import Article


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name='评论内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.user.username + '的回复'

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = verbose_name


# todo image的模型
class Image(models.Model):
    image = models.ImageField(upload_to='image/')
