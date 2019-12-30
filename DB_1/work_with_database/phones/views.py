from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort')
    data = Phone.objects.all()
    if sort_by == 'name':
        data = Phone.objects.order_by('name')
    if sort_by == 'min_price':
        data = Phone.objects.order_by('price')
    if sort_by == 'max_price':
        data = Phone.objects.order_by('-price')
    context = {
        'data': data
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
