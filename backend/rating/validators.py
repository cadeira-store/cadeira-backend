from django.core.exceptions import ValidationError


def validate_rating(rating):
    if type(rating) != int or not 1 <= rating <= 5:
        raise ValidationError(
            'Рейтинг должен быть целым числом в диапазоне от 1 до 5')
