from django.core.validators import RegexValidator
import re

from django.core.exceptions import ValidationError

phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")


def validate_real_name(value):
    """
    Метод проверяет соответствует ли имя и фамилия
    пользователя заданному регулярному выражению.
    Если нет - выбрасывает ValidationError.
    """
    reg = r'^[\w-]+\Z'

    if not re.fullmatch(reg, value):
        raise ValidationError({
            'Недопустимое значение имени {value}'})
