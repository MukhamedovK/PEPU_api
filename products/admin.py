from django.contrib import admin
from .models import Size, Product, Category, ProductPhoto


admin.site.register(Size)
admin.site.register(Category)
admin.site.register(ProductPhoto)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


