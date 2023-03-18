from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers


def upload_to_uPhoto(instance, filename):
    return 'images/users/{filename}'.format(filename=filename)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    gender = models.CharField(
        max_length=140,
        null=True,
        choices=(
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        )
    )
    birth_date = models.DateField(null=True, blank=True)
    pro = models.BooleanField(default=False)
    phone = models.TextField(null=True, unique=True)
    photo = models.ImageField(upload_to=upload_to_uPhoto, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return self.email


def upload_to_catalog(instance, filename):
    return 'images/catalog/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.DO_NOTHING)
    model = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, related_name="products", on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to=upload_to_catalog, blank=True, null=True)

    def __str__(self):
        return self.model


class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductOrder')
    order_date = models.DateField()
    pay_status = models.CharField(
        default='Не оплачен',
        null=False,
        max_length=15,
        choices=(
            ('Не оплачен', 'Не оплачен'),
            ('Оплачен', 'Оплачен'),
        )
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return f'order #{self.pk} - {self.order_date}'


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, related_name='product_orders', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='product_orders', on_delete=models.CASCADE)
    delivery_satus = models.CharField(
        default='Обрабатывается',
        null=False,
        max_length=15,
        choices=(
            ('Обрабатывается', 'Обрабатывается'),
            ('В доставке', 'В доставке'),
            ('Доставлен', 'Доставлен'),
        )
    )
    delivery_address = models.CharField(max_length=100)
    total_quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)


class Coupon(models.Model):
    code = models.CharField(max_length=255, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateTimeField()
    category = models.ForeignKey(Category, related_name="coupons", on_delete=models.CASCADE)


class Review(models.Model):
    user = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=((1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')))
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
