from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.AdminSite):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.AdminSite):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product)
admin.site.register(Category)