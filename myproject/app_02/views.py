from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Product, Order
from .forms import CustomerForm, ProductForm, OrderForm
from datetime import datetime, timedelta


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
        form = ProductForm(request.POST, request.FILES)
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
        form = ProductForm(request.POST, request.FILES, instance=product)
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


def items_ordered_within_time_range(request, customer_id, time_range):
    customer = get_object_or_404(Customer, id=customer_id)
    today = datetime.now().date()

    if time_range == 'week':
        start_date = today - timedelta(days=7)
    elif time_range == 'month':
        start_date = today - timedelta(days=30)
    elif time_range == 'year':
        start_date = today - timedelta(days=365)
    else:
        return HttpResponseBadRequest("Invalid time range")

    ordered_products = Product.objects.filter(order__customer=customer,
                                              order__placement_date__gte=start_date).distinct()

    return render(request, 'app_02/items_ordered_list.html',
                  {'customer': customer, 'ordered_products': ordered_products})
