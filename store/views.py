from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView
from .models import Product, Category, Order, OrderItem
from .forms import AddToCartForm, RegisterForm

class ProductListView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        qs = Product.objects.filter(active=True).select_related("category")
        slug = self.request.GET.get("category")
        if slug:
            qs = qs.filter(category__slug=slug)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = Category.objects.all()
        ctx["selected_category"] = self.request.GET.get("category")
        return ctx

class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = AddToCartForm()
        return ctx

class AddToCartView(LoginRequiredMixin, FormView):
    form_class = AddToCartForm
    template_name = "store/product_detail.html"

    def form_valid(self, form):
        product_slug = self.kwargs["slug"]
        product = get_object_or_404(Product, slug=product_slug, active=True)
        order, _ = Order.objects.get_or_create(user=self.request.user, status="cart")
        item, created = OrderItem.objects.get_or_create(
            order=order, product=product, defaults={"unit_price": product.price, "quantity": 0}
        )
        item.quantity += form.cleaned_data["quantity"]
        if item.unit_price != product.price:
            item.unit_price = product.price
        item.save()
        messages.success(self.request, "Produto adicionado ao carrinho.")
        return redirect("store:cart")

class CartView(LoginRequiredMixin, TemplateView):
    template_name = "store/cart.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        order = Order.objects.filter(user=self.request.user, status="cart").prefetch_related("items__product").first()
        ctx["order"] = order
        return ctx

class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = "store/checkout.html"

    def post(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user, status="cart").first()
        if not order or order.items.count() == 0:
            messages.error(request, "Seu carrinho está vazio.")
            return redirect("store:cart")
        order.status = "submitted"
        order.save()
        messages.success(request, "Pedido enviado com sucesso!")
        return redirect("store:orders")

class OrdersView(LoginRequiredMixin, ListView):
    template_name = "store/orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).exclude(status="cart").prefetch_related("items__product")

class RegisterView(FormView):
    template_name = "store/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("store:product_list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Cadastro realizado. Faça login para continuar.")
        return super().form_valid(form)
