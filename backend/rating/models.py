from django.db import models
from django.conf import settings
from products.models import Product
from .validators import validate_rating


class Rating(models.Model):
    """
    Модель рейтинга товаров.
    Рейтинг может быть только целым числом в диапазоне от 1 до 5ю
    Пользователь может поставить товару только одну оценку.
    Общий рейтинг товара расчитывается как среднее значение.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE)
    rating = models.SmallIntegerField(
        verbose_name='Оценка пользователя',
        validators=[validate_rating],
        blank=False)
