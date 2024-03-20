from django.db import models


class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    cust_id = models.IntegerField()
    invoice_date = models.CharField(max_length=10)
    due_date = models.CharField(max_length=10)
    total_amt = models.CharField(max_length=40)
    status = models.CharField(max_length=75)
    pay_id = models.IntegerField()
    
    class Meta:
        db_table = "invoices"


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=50)
    login_id = models.IntegerField(max_length=10)
    ph = models.IntegerField(max_length=50)

    class Meta:
        db_table = "customers"

class Item(models.Model):
    invoice_id = models.IntegerField()
    item_name = models.CharField(max_length=20)
    item_price = models.IntegerField()
    id = models.AutoField(primary_key=True)
    class Meta:
        db_table = "items"



class Payments(models.Model):

    pay_id = models.IntegerField(primary_key=True)
    bank_name = models.CharField(max_length=20, null=True)
    account_no = models.CharField(max_length=25, null=True)
    isfc = models.CharField(max_length=15, null=True)

    class Meta:
        db_table="payments"


