from django.contrib import admin
from .models import Place, Category, Product, Storehouse


admin.site.register(Place)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_active')
    readonly_fields = ('created_date',)
    list_filter = ('category', 'is_active')


@admin.register(Storehouse)
class StorehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'product', 'place')
    readonly_fields = ('created_date',)
    list_filter = ('account', 'place')
