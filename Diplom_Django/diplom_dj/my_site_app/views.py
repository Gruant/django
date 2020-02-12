from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import ReviewForm, SignupForm
from django.core.paginator import Paginator
from .models import Product, ProductOrder, Review, Category, Collection, Order, ProductInBasket, Basket


def home(request):
    template = 'index.html'
    collections_data = Collection.objects.all().order_by('-created').prefetch_related('products')
    collections = []
    for collection in collections_data:
        products = []
        for product in collection.products.all():
            products.append({'name': product.title, 'image': product.image, 'price': product.price,
                             'slug': product.slug, 'product_id': product.id})
        collections.append({'name': collection.title, 'description': collection.description, 'products': products})

    context = {
        "collections": collections,
    }

    return render(request, template, context)


def view_logout(request):
    logout(request)
    return redirect('home')


def view_signup(request):
    if request.method == 'POST':
        register_form = SignupForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:
        register_form = SignupForm()

    context = {
        'form': register_form
    }

    return render(
        request,
        'signup.html',
        context
    )


def view_category(request, pk):
    template = 'smartphones.html'

    context = dict()
    category = Category.objects.get(id=pk)
    context['categories'] = category

    page = request.GET.get('page')
    page = 1 if not page else int(page)

    posts = Product.objects.filter(category=pk)

    paginator = Paginator(posts, 2)

    if page > paginator.num_pages:
        page = 1

    context['products'] = paginator.page(page)
    return render(request, template, context=context)


def product_detail(request, product_slug):
    template = 'phone.html'
    try:
        user_uid = get_uid(request)
        product = Product.objects.get(slug=product_slug)
        review_data = Review.objects.filter(product=product).all()

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data['description']
                rating = form.cleaned_data['mark']
                author = form.cleaned_data['name']
                user, created = User.objects.get_or_create(username=user_uid)
                user.first_name = author
                user.save()
                Review.objects.create(text=text, rating=rating, author=user, product=product)
                return redirect('product_detail', product_slug=product.slug)

        else:
            form = ReviewForm()
        reviews = review_data.all().order_by('-id')
        context = {
            'product_data': product,
            'reviews': reviews,
            'form': form
        }
    except ObjectDoesNotExist:
        context = {}

    return render(request, template, context)


def get_uid(request):
    if not request.user.is_authenticated:
        uid = request.session.session_key
        if not uid:
            uid = request.session.cycle_key()
    else:
        uid = request.user.username
    return uid


def get_basket(uid):
    basket, created = Basket.objects.get_or_create(uid=uid)
    return basket


def basket_view(request):
    context = dict()
    basket = get_basket(get_uid(request))
    context['basket'] = ProductInBasket.objects.filter(basket=basket).select_related('product')
    return render(request, 'cart.html', context=context)


def add_to_basket(request, product_id):
    basket = get_basket(get_uid(request))
    product = Product.objects.get(id=product_id)

    product_in_basket = ProductInBasket.objects.filter(basket=basket, product=product)

    if product_in_basket:
        my_obj = product_in_basket.first()
        my_obj.count += 1
        my_obj.save()
    else:
        ProductInBasket.objects.create(basket=basket, product=product, count=1)

    return redirect(basket_view)


def order_creation(request):
    user_uid = get_uid(request)
    basket = get_basket(user_uid)
    products = basket.items.all()

    if products:
        user, created = User.objects.get_or_create(username=user_uid)
        order = Order.objects.create(buyer=user, total=0)
        for product in products:
            item = ProductInBasket.objects.get(product=product, basket=basket)
            ProductOrder.objects.create(product=product, order=order, total=(product.price * item.count),
                                        count=item.count)
            order.total += product.price * item.count
            order.save()
            item.delete()
    return redirect('home')



