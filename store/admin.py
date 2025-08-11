from django.contrib import admin
from .models import product,Variation,ReviewRating

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date')
    prepopulated_fields = {'slug':('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active')
    list_editable =('is_active',)
    list_filter = ('product','variation_category','variation_value')

admin.site.register(product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(ReviewRating)
