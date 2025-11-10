from django.urls import path
from .views import (
    ProductListView, ProductDetailView, AddToCartView,
    CartView, CheckoutView, OrdersView, RegisterView
)

app_name = "store"

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("produto/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("produto/<slug:slug>/adicionar/", AddToCartView.as_view(), name="add_to_cart"),
    path("carrinho/", CartView.as_view(), name="cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("pedidos/", OrdersView.as_view(), name="orders"),
    path("register/", RegisterView.as_view(), name="register"),
]
