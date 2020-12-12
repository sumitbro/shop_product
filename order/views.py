from django.shortcuts import render
from .models import Product, Customer, Order

# Create your views here.
def home(request):

    orders= Order.objects.all()
    cust= Customer.objects.all()

    total_cust= cust.count()
    total_order= orders.count()
    delivered= orders.filter(status='Delivered').count()
    pending= orders.filter(status='pending').count()


    context={
        'orders':orders,
        'cust':cust,
        
        'total_order':total_order,
        'delivered':delivered,
        'pending':pending

    }

    return render(request,'dashboard.html', context)


def product(request):

    pro= Product.objects.all()

    return render(request, 'product.html',{'pro':pro})


def customer(request,id):

    cus= Customer.objects.get(id=id)
    order= cus.order_set.all()
    total_order= order.count()
    context= {'cus':cus,'order':order, 'total_order':total_order}


    return render(request, 'customer.html',context)
