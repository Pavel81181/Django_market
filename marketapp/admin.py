from django.contrib import admin
from .models import User, Product, Order
@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(stock=0)



class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['name', 'price', 'stock']
    ordering = ['name']
    list_filter = ['add_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]


    """Отдельный продукт."""
    # fields = ['name', 'description', 'price', 'add_date', 'rating']
    readonly_fields = ['add_date', 'name']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара и дата добавления',
                'fields':['description', 'add_date'],
        },
        ),
        (
            'Цена и остаток',
            {
                'fields': ['price', 'stock'],

            }
        ),

    ]


class UserAdmin(admin.ModelAdmin):
    """Список клиентов"""
    list_display = ['name', 'register_date']
    ordering = ['name']
    list_filter = ['phone', 'email']
    search_fields = ['address']
    search_help_text = 'Поиск по полю Адрес'

    """Отдельный клиент."""
    # fields = ['name', 'email', 'phone', 'address', 'register_date']
    readonly_fields = ['register_date', 'name']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контактная информация',
            {
                'classes': ['collapse'],
                'description': 'Контактная информация по клиенту',
                'fields': ['email', 'phone', 'address'],
            },
        ),
        (
            'Дата регистрации',
            {
                'fields': ['register_date'],

            }
        ),

    ]


class OrderAdmin(admin.ModelAdmin):
    """Список заказов"""
    list_display = ['customer', 'date_ordered', 'total_price']
    ordering = ['total_price', '-customer']
    list_filter = ['customer', 'total_price']
    search_fields = ['products']
    search_help_text = 'Поиск по Товарам'

    """Отдельный заказ."""
    # fields = ['customer', 'products', 'date_ordered', 'total_price']
    readonly_fields = ['customer', 'products', 'date_ordered', 'total_price']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Заказанные товары',
            {
                'classes': ['collapse'],
                'description': 'Заказанные товары',
                'fields': ['products'],
            },
        ),
        (
            'Дата регистрации и сумма заказа',
            {
                'fields': ['date_ordered', 'total_price'],

            }
        ),

    ]

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
