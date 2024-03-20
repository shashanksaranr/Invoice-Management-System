from django.shortcuts import render,redirect, get_object_or_404
from .models import Invoice
from .forms import InvoiceForm
from .forms import ItemForm
from .models import Customer
from .models import Item
from .models import Customer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Payments


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('invoice-list/')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')



def index(request):
    return render(request,'show.html')



def invoice_list(request):
    
    invoices = Invoice.objects.all()
    return render(request,'invoicelist.html',{'invoice': invoices})




def add_invoice(request):
    if request.method == 'POST':
        invoice_id = request.POST.get('invoice_id', None)
        cust_id = request.POST['cust_id']
        invoice_date = request.POST['invoice_date']
        due_date = request.POST['due_date']
        total_amt = request.POST['total_amt']
        status = request.POST['status']
        pay_id = request.POST['pay_id']

        if invoice_id is None:
            # Display an error message and render the form again
            error_message = 'Invoice ID is required.'
            return render(request, 'add_invoice.html', {'error_message': error_message})

        # Save data to the database
        Invoice.objects.create(
            invoice_id=invoice_id,
            cust_id=cust_id,
            invoice_date=invoice_date,
            due_date=due_date,
            total_amt=total_amt,
            status=status,
            pay_id=pay_id
        )
        return redirect('/invoice-list')
    return render(request, 'add_invoice.html')


def edit_invoice(request, invoice_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to edit or delete invoices.')
        return redirect('invoice-list/')
    invoice = get_object_or_404(Invoice, invoice_id=invoice_id)

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('/invoice-list')
    else:
        form = InvoiceForm(instance=invoice)

    return render(request, 'edit_invoice.html', {'form': form, 'invoice': invoice})



def delete_invoice(request,invoice_id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to edit or delete invoices.')
        return redirect('/invoice-list')
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoice.delete()
    return redirect('/invoice-list')


def customer_details(request, cust_id):
    customer = get_object_or_404(Customer, cust_id=cust_id)
    return render(request, 'customer_details.html', {'customer': customer})


def invoice_items(request, invoice_id):
    inv_id=invoice_id
    products = Item.objects.filter(invoice_id=invoice_id)
    return render(request, 'invoice_items.html', {'products': products,'inv_id': inv_id})


def add_customer(request):
    if request.method == 'POST':
        cust_id = request.POST.get('cust_id', None)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_id = request.POST['email_id']
        login_id=request.POST['login_id']
        ph = request.POST['ph']

        if cust_id is None:
            # Display an error message and render the form again
            error_message = 'Customer ID is required.'
            return render(request, 'add_customer.html', {'error_message': error_message})

        # Save data to the database
        Customer.objects.create(
            cust_id=cust_id,
            last_name=last_name,
            first_name=first_name,
            email_id=email_id,
            login_id=login_id,
            ph=ph,
        )

        return redirect('/invoice-list')

    return render(request, 'add_customer.html')


def delete_item(request,id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to edit or delete item.')
        return redirect('/invoice-list')
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('/invoice-list')



def edit_item(request,id):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to edit or delete items.')
        return redirect('item-list/')
    item = get_object_or_404(Item, pk=id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/invoice-list')
    else:
        form = ItemForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'item': item})



def add_item(request, id):
    if request.method == 'POST':
        item_invoiceid=id
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        item_id=request.POST.get('item_id')
        item = Item(invoice_id=item_invoiceid,item_name=item_name,item_price=item_price,id=item_id)
        item.save()
        return redirect('/invoice-list')

    return render(request, 'add_item.html')

def payment(request, pay):
    payments = Payments.objects.filter(pay_id=pay)
    return render(request, 'payments.html', {'payments': payments})
