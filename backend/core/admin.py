from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.ProductOrder)
admin.site.register(models.Coupon)
admin.site.register(models.Review)
admin.site.register(models.Category)
admin.site.register(models.Brand)
