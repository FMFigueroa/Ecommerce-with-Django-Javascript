from django.contrib import admin
from .models import Products
from .models import Order
# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Afesk"
admin.site.index_title = "Manager Ecommerce"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description = 'Default Category'
    list_display = ('title','price','discount_price','category','image')
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    fields = ('title','price')
    list_editable = ('price',)


admin.site.register(Products,ProductAdmin)
admin.site.register(Order)

