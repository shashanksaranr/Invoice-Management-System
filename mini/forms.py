from django import forms
from .models import Invoice
from .models import Item


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['invoice_id','item_name', 'item_price', 'id']
