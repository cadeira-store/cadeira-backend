from django.conf import settings
from django.contrib.auth.models import AbstractUser

from .validators import phone_number_regex, validate_real_name
from django.db import models


class User(AbstractUser):
    """
    Модель для регистрации и авторизации пользователя на сайте.
    Вход через почту и пароль.
    """
    email = models.EmailField(
        'Email',
        max_length=settings.EMAIL_MAX_LENGTH,
        unique=True)
    first_name = models.CharField(
        'Имя',
        max_length=settings.USER_MAX_LENGTH,
        validators=[validate_real_name],
        blank=False)
    phone_number = models.CharField(
        'Номер телефона',
        validators=[phone_number_regex],
        max_length=16,
        unique=True)
    password = models.CharField(
        'Пароль',
        max_length=settings.USER_MAX_LENGTH)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name
