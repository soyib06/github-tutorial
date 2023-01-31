from django.shortcuts import render, redirect
from .models import * 
from django.contrib.auth.decorators import login_required 
from .forms import RateForm
from django.db.models import Q

@login_required(login_url='/users/sign_in')
def store(request):
    search = request.GET.get('search')
    products = Product.objects.all()
    products = products.filter(Q(name__icontains=search) )if search else products
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)

def  product_detail(request, pk):
     product = Product.objects.get(pk=pk)
     if request.user.is_authenticated:
         if not product.view_set.filter(user = request.user).exists():
            product.view_set.create(user = request.user)
     
     product = Product.objects.get(pk=pk)
     return render(request, 'store/product_detail.html', {'product': product})
 

def rate_product(request, pk):
        product = Product.objects.get(pk=pk)
        reviews = Review.objects.filter(product=product)

        if request.method == 'POST':
            form = RateForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.user = request.user
                rating.product = product
                rating.save()
                return redirect('rate_product', pk=pk)
        form = RateForm()
        return render(request, 'store/rate.html', {'form': form, 'product': product, 'reviews': reviews}) 


def products_list(request):    
    products = Product.objects.all()       
    return render(request, 'product_list.html', {'products': products, })

 