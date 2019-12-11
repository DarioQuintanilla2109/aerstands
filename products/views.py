from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django_countries import countries
from django.shortcuts import render
from .models import Inventory
from .choices import oem, weight, price

def index(request):
    products = Inventory.objects.all().order_by('-list_date').filter(is_available=True)
    country_choices = list(countries)

    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'products': paged_listings,
        'oem': oem,
        'weight': weight,
        'price': price,
        'country': country_choices
    }
    return render(request, 'products/products.html', context)

def filter(request):
    return render(request, 'products/filter.html')
