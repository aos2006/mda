from django.contrib import admin
from .models import Product, Category, Color, Tag, ProductCategory, ProductColor, ProductTag

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(ProductTag)
admin.site.register(ProductColor)
admin.site.register(ProductCategory)
# Register your models here.
