from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display=('id', 'order_number', 'customer_name', 'total_amount')


admin.site.register(Order, OrderAdmin)
