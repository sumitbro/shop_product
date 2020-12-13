from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import Product, Customer, Order
from .forms import OrderForm


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




def createview(request, id):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
	cus = Customer.objects.get(id=id)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=cus)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=cus)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'create.html', context)














# def createview(request,id):
#     OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
#     cus= Customer.objects.get(id=id)
#     formset= OrderFormSet(instance=cus)

#     formset= OrderForm(initial={'customer':cus})
    

#     if request.method=="POST":
#         formset= OrderFormSet(request.POST, instance=cus)
#         if formset.is_valid:
#             formset.save()
#             return redirect('/')
        
        
#     context={'form':formset}
#     return render(request, 'create.html', context)

def updateorder(request, id):
    order= Order.objects.get(id=id)
    form= OrderForm(instance=order)
    
    if request.method=="POST":
        form= OrderForm(request.POST, instance=order)
        form.save()
        return redirect('/')

    context={'form':form}
    return render(request, 'update.html', context)


def deleteorder(request, id):
    order= Order.objects.get(id=id)
    if request.method=="POST":
        order.delete()
        return redirect('/')

    context={'item':order}
    return render(request, 'delete.html',context)
