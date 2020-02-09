"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from my_site_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registration/login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.view_signup, name='signup'),
    path('logout/', views.view_logout, name='logout'),
    path('cart/', views.basket_view, name='basket'),
    path('product/<product_slug>/', views.product_detail, name='product_detail'),
    path('category/<pk>/', views.view_category, name='category'),
    path('basket/', views.basket_view, name='basket_view'),
    path('add_to_basket/<product_id>/', views.add_to_basket, name='add_to_basket'),
    path('order_creation', views.order_creation, name='order_creation')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

