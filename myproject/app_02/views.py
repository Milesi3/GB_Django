from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Product, Order
from .forms import CustomerForm, ProductForm, OrderForm


# Это предположительные функции, но для проверки надо как то научиться дружить с html
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to customer list view
    else:
        form = CustomerForm()
    return render(request, 'app_02/customer_form.html', {'form': form})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'app_02/product_form.html', {'form': form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'app_02/customer_list.html', {'customers': customers})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'app_02/product_list.html', {'products': products})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'app_02/order_list.html', {'orders': orders})


def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'app_02/customer_form.html', {'form': form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'app_02/product_form.html', {'form': form})


def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'app_02/customer_confirm_delete.html', {'customer': customer})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'app_02/product_confirm_delete.html', {'product': product})
