from django.contrib import admin
from .models import Customer, Product, Order

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'registration_date')
    list_filter = ('registration_date',)
    list_per_page = 20
    search_fields = ('name', 'email', 'phone_number')
    fieldsets = (
        ('Customer Information', {
            'fields': ('name', 'email', 'phone_number', 'address')
        }),
        ('Registration Information', {
            'fields': ('registration_date',)
        }),
    )

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'addition_date')
    list_filter = ('addition_date',)
    list_per_page = 20
    search_fields = ('name', 'description')
    readonly_fields = ('addition_date',)

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_amount', 'placement_date')
    list_filter = ('placement_date',)
    list_per_page = 20
    search_fields = ('customer__name',)
    fieldsets = (
        ('Order Information', {
            'fields': ('customer', 'products', 'total_amount')
        }),
        ('Placement Information', {
            'fields': ('placement_date',)
        }),
    )

admin.site.register(Order, OrderAdmin)
