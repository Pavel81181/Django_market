from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),                                            #вывод главной страницы
    path('products/', views.products, name='products'),                        #вывод списка всех товаров
    path('product/<int:id_product>', views.product, name='product'),           #вывод выбранного пользователем проодукта по id
    path('order/<int:id_order>', views.order, name='order'),                   # вывод заказа по Id
    path('users/', views.users, name='users'),                           # вывод всех клиентов
    path('orders/', views.orders, name='orders'),                              # вывод всех заказов
    path('user_orders/<int:user_id>', views.user_orders, name='user_orders'),      # все заказы по клиенту
    path('user_products_sorted/<int:user_id>/<int:days>/', views.user_products_sorted, name='user_products_sorted'), # вывод всех товаров по клиенту за последние кол дней
    path('product_form/<int:id_product>', views.product_form, name='product_form'),        #форма дляизменения выбранного по id продукта (форма для выбора Id продукта  - стр 15)
                                            # форма для выбора id продукции для вывода на страницу
]
