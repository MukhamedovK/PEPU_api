from django.contrib import admin
from .models import Size, Product, Category


admin.site.register(Size)
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


