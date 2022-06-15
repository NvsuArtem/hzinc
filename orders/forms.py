from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email',]


