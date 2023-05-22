from django.db import models
from django.conf import settings


class Comment(models.Model):
    """
    Модель комментариев-отзывов о товарах.
    К комментарию можно прикрепить картинки.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='comments')
    title = models.CharField(
        'Заголовок',
        max_length=100)
    text = models.CharField(
        'Текст',
        max_length=1000)


class CommentImage(models.Model):
    """
    Модель дл хранения фотографий из комментария.
    У каждого комментария может быть несколько фотографий.
    """
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        verbose_name='Комментарий',
        related_name='images')
    image = models.ImageField(
        upload_to='rating/images',
        default=None,
        null=False,
        verbose_name='Фотография из комментария')
