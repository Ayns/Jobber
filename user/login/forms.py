from .models import customer
from django.forms import ModelForm


class customerForm(ModelForm):
    class meta:
        model = customer
        fields = ['customer','city','gst']
        