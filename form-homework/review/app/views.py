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

    if not request.session.get('reviewed_products'):
        request.session['reviewed_products'] = list()

    form = ReviewForm
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(text=form.cleaned_data['text'], product=product)
            request.session['reviewed_products'].append(product.id)
            return redirect('product_detail', pk=product.id)

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
