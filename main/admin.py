from django.contrib import admin

from .models import Product, Category

admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price',
                    'image', 'available', 'created', 'updated', 'discount'
                    ]
    list_filter = ['available', 'created', 'updated', 'discount']

    list_editable = ['price', 'available', 'discount']
    prepopulated_fields = {'slug': ('name',)}
