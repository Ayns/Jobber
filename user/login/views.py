from django.shortcuts import render, redirect
from .forms import customerForm

# Create your views here.

def home(request):
    template = 'index.html'
    context = {}
    return render(request, template,context)




def add_customer(request):
    if request.method=="POST":
        form = customerForm(request.POST)
        if form.is_valid():
            cust = form.save(commit=False)
            cust.save()
    else:
        form = customerForm()
    return render(request,'customer.html', {'form': form})

    
