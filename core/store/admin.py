from django.contrib import admin
from .models import (Category, Computer, Smartphone, 
                    Furniture, Clothes, Shoes)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


class ComputerAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_order',
                    'computer_or_laptop', 'created']
    prepopulated_fields = {'slug': ('name',)}


class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_order',
                    'operating_system', 'matrix_type',
                    'created']
    prepopulated_fields = {'slug': ('name',)}


class FurnitureAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_order',
                    'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


class ClothesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_order',
                    'brand', 'gender', 'country_of_origin',
                    'created']
    prepopulated_fields = {'slug': ('name',)}


class ShoesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_order',
                    'brand', 'size', 'created']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Clothes, ClothesAdmin)
admin.site.register(Shoes, ShoesAdmin) 