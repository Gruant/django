from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    is_review_exist = True

    form = ReviewForm
    if request.method == 'POST':
        review_text, product_review = request.POST.get('text'), request.POST.get('product')
        Review.objects.create(text=review_text, product=product)
        request.session['reviewed_products'].append(product.id)

    if product.id in request.session['reviewed_products']:
        is_review_exist = True

    review = Review.objects.filter(product=product)
    context = {
        'form': form,
        'reviews': review,
        'product': product,
        'is_review_exist': is_review_exist
    }

    return render(request, template, context)
