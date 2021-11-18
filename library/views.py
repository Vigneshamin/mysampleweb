from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        #print(form)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'library/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.info(request, "Username OR password is incorrect")
    context = {}
    return render(request, 'library/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders, 'customers':customers,
               'total_customer':total_customers,'total_orders':total_orders,
               'delivered':delivered,'pending':pending}
    return render(request, 'library/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    customer = request.user.customer
    id = customer.id
    for ord in orders:
        id = ord.customer.id
        #print(id)
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders,
               'total_orders':total_orders,
               'id':id,
               'delivered':delivered,'pending':pending}
    return render(request, 'library/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def librarySettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    #print(form)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'library/library_settings.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, 'library/products.html', {'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, c_id):
    customer = Customer.objects.get(id=c_id)
    orders = customer.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'customer':customer,'orders':orders ,'order_count':order_count,'myFilter':myFilter}
    return render(request, 'library/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=1,can_delete=False)
    customer = Customer.objects.get(id=id)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST:',request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return  redirect('/')
    context = {'formset':formset}
    #print(context)
    return render(request, 'library/order_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'library/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'library/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def createOrderCust(request,id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', ), extra=1,can_delete=False)
    customer = Customer.objects.get(id=id)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    products = Product.objects.all()
    #form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST:',request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return  redirect('/')
    context = {'formset':formset,'products':products}
    #print(context)
    return render(request, 'library/cust_order_form.html',context)
