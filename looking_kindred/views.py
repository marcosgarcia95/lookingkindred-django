#created manually
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
current_year = datetime.now().year
from store.models import Product

def Home(request):
    products = Product.objects.all().filter(is_available=True)
    context_dict = {
        'products': products,
        'year':current_year,
        'company_name': 'Looking Kindred',
    }
    return render(request, 'home.html', context = context_dict)