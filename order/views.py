from django.shortcuts import render, redirect
from django.forms import inlineformset_factory


from .models import Product, Customer, Order
from .forms import OrderForm, CustomerForm
from django.contrib.auth.decorators import login_required
from .filters import OrderFilter
from .decorators import allowed_users,admin_only



# Create your views here.
# login_required(login_url="signin")
@login_required(login_url="/account/signin" )
@admin_only
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

@login_required(login_url="/account/signin" )
@allowed_users(allowed_roles=['admin'])
def product(request):

    pro= Product.objects.all()

    return render(request, 'product.html',{'pro':pro})

@login_required(login_url="/account/signin" )
@allowed_users(allowed_roles=['admin'])
def customer(request,id):

    cus= Customer.objects.get(id=id)
    order= cus.order_set.all()
    total_order= order.count()
    myFilter= OrderFilter(request.GET, queryset=order)
    order= myFilter.qs

    context= {'cus':cus,'order':order, 'total_order':total_order,'myFilter':myFilter}


    return render(request, 'customer.html',context)



@login_required(login_url="/account/signin" )
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url="/account/signin" )
@allowed_users(allowed_roles=['admin'])
def updateorder(request, id):
    order= Order.objects.get(id=id)
    form= OrderForm(instance=order)
    
    if request.method=="POST":
        form= OrderForm(request.POST, instance=order)
        form.save()
        return redirect('/')

    context={'form':form}
    return render(request, 'update.html', context)

@login_required(login_url="/account/signin" )
@allowed_users(allowed_roles=['admin'])
def deleteorder(request, id):
    order= Order.objects.get(id=id)
    if request.method=="POST":
        order.delete()
        return redirect('/')

    context={'item':order}
    return render(request, 'delete.html',context)



@login_required(login_url="/account/signin" )
@allowed_users(allowed_roles=['customer'])
def userpage(request):
    order= request.user.customer.order_set.all()
    

    context={'order':order}

    return render(request, 'user.html', context)




# @login_required(login_url="/account/signin")
# @allowed_users(allowed_roles=['customer'])
# def account(request):
# 	customer = request.user.customer
# 	form = CustomerForm(instance=customer)

# 	if request.method == 'POST':
# 		form = CustomerForm(request.POST, request.FILES, instance=customer)
# 		if form.is_valid():
# 			form.save()


# 	context = {'form':form}
# 	return render(request, 'account.html', context)
