from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def ratingCheck(value):
    if value < 0 or value > 5:
        raise ValidationError(
            _('%(value)s must be bigger than 0 and less or equal 5'),
            params={'value': value}
        )

class Color(models.Model):
    color = models.CharField(max_length=32)
    class Meta:
        db_table = "colors"

class Tag(models.Model):
    title = models.CharField(max_length=32)
    class Meta:
        db_table = "tags"

class Category(models.Model):
    title = models.CharField(max_length=32)
    class Meta:
        db_table = "categories"

class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    rating = models.FloatField(validators=[ratingCheck])
    description = models.TextField()
    likes = models.IntegerField()
    quantity = models.IntegerField()
    class Meta:
        db_table = "products"

class ProductTag(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    class Meta:
        db_table = "product_tag"

class ProductColor(models.Model):
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        db_table = "product_color"

class ProductCategory(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        db_table = "product_category"

