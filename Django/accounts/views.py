from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers =Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()
    return render(request, 'accounts/dashboard.html', {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'deliverd':delivered, 'pending':pending})


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products' : products})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    return render(request, 'accounts/customer.html',{'customer':customer, 'orders':orders, 'orders_count':orders_count})


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/order_form.html', {'form':form})


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/order_form.html', {'form':form})


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    return render(request, 'accounts/delete.html', {'item':order})