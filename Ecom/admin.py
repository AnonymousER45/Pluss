from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Product,Category,subCategory,Cart ,CartProduct,Wishlist,WishlistProduct,Banner,ProductUnavailable,Requestbook,EcomOrder,Exchange_return,Refund_bankdetails,Refund_upidetails

class ProductAdmin(ImportExportModelAdmin):
    list_display = ("id","title","Category","subCategory")
    list_filter = ['Category','subCategory']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ['name']

class SubCateoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    list_filter = ['name']

class EcomOrderAdmin(admin.ModelAdmin):
    list_filter = ['date_of_ordering']

admin.site.register(EcomOrder,EcomOrderAdmin),

admin.site.register(Product,ProductAdmin),
admin.site.register(Category,CategoryAdmin),
admin.site.register(subCategory,SubCateoryAdmin),
admin.site.register(Banner),
admin.site.register(ProductUnavailable),
admin.site.register(Requestbook),

admin.site.register(Cart),
admin.site.register(CartProduct),


admin.site.register(Wishlist),
admin.site.register(WishlistProduct),


admin.site.register(Exchange_return),
admin.site.register(Refund_bankdetails),
admin.site.register(Refund_upidetails),


