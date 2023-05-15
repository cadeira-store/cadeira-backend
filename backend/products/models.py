from django.db import models


class Product(models.Model):
    """
    В продукте хранится только заглавная фотография товара и поля,
    необходимые для отображения в списке товаров.
    Все остальные хранятся в продакт инфо тк они нужны только при просмотре
    карточки товара.
    """
    name = models.CharField(
        verbose_name='Название',
        max_length=200)
    price = models.PositiveSmallIntegerField(
        verbose_name='Цена')
    oldprice = models.PositiveSmallIntegerField(
        verbose_name='Старая цена')
    percent = models.PositiveSmallIntegerField(
        verbose_name='Скидка')
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='products/images')
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Категория')
    vendor = models.ForeignKey(
        'Vendor',
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Производитель')
    material = models.CharField(
        verbose_name='Материал',
        max_length=200)
    color = models.CharField(
        verbose_name='Цвет',
        max_length=200)
    length_mm = models.PositiveSmallIntegerField(
        verbose_name='Длина')
    width_mm = models.PositiveSmallIntegerField(
        verbose_name='Ширина')
    height_mm = models.PositiveSmallIntegerField(
        verbose_name='Высота')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категория товара',
        max_length=200)


class Vendor(models.Model):
    name = models.CharField(
        verbose_name='Производитель',
        max_length=200)


class ProductDescription(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='product_info',
        verbose_name='Товар')
    # rate = models.FloatField(
    #     verbose_name='Рейтинг')
    barcode = models.CharField(
        verbose_name='Код товара',
        max_length=200)
    weight = models.FloatField(
        verbose_name='Вес')
    warranty_days = models.PositiveSmallIntegerField(
        verbose_name='Гарантия')
    stock = models.PositiveSmallIntegerField(
        verbose_name='В наличии')
    leadtime = models.PositiveSmallIntegerField(
        verbose_name='Хз что это, уточнить у Темы')
    availability = models.BooleanField(
        verbose_name='Доступно')
    material = models.CharField(
        verbose_name='Материал',
        max_length=200)
    material_secondary = models.CharField(
        verbose_name='Материал допольнительно',
        max_length=200)
    color = models.CharField(
        verbose_name='Цвет',
        max_length=200)
    base_material = models.CharField(
        verbose_name='Материал основания',
        max_length=200)
    base_color = models.CharField(
        verbose_name='Цвет основания',
        max_length=200)
    nearest_delivery_date = models.DateField(
        verbose_name='Ближайшая дата доставки')
    service_life = models.PositiveSmallIntegerField(
        verbose_name='Срок службы')
    country_of_origin = models.CharField(
        verbose_name='Страна производства',
        max_length=200)
