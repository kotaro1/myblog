from django.db import models
from django.utils import timezone


class Category(models.Model):
    """記事のカテゴリ"""

    name = models.CharField('カテゴリ', max_length=30)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    """ポスト"""

    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """記事へのコメント"""

    name = models.CharField('お名前', max_length=30, default='匿名希望')
    text = models.TextField('コメント')
    post = models.ForeignKey(Post, verbose_name='紐づく記事', on_delete=models.PROTECT)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:10]
