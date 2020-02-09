from django.contrib import admin
from mptt.admin import MPTTModelAdmin
import admin_thumbnails
from .models import Product, Category, Collection, Order, ProductOrder


@admin_thumbnails.thumbnail('image', append=False, width='100px', height='100px')
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'price', 'image')
        }),
        ('Категория', {
            'fields': ('category',)
        }),
    )
    list_display = ('title', 'category', 'price', 'image_thumbnail')
    list_filter = ('title', 'category', 'price')


class CategoryAdmin(MPTTModelAdmin):
    fields = ('name', 'parent')
    list_display = ('name',)


class CollectionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description',)
        }),
        ('Категория', {
            'fields': ('products',)
        }),
    )
    list_display = ('title',)


class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductOrderInline]
    fields = ('buyer', 'total')
    list_display = ('buyer', 'total')
    list_filter = ('total', 'buyer')


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)