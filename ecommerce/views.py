



from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .models import Product, TipResource, TeamMember   # importing models
import json

# Homepage view
def homepage(request):
    return render(request, 'ecommerce/index.html')

# Products page view
def products(request):
    # Fetch all active products from the database
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'ecommerce/products.html', {'products': products})

# Product detail view
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)  # Fetch the product using its slug
    return render(request, 'ecommerce/product_detail.html', {'product': product})

# Tips and Resources page view
def tipsandresources(request):
    # Fetch all active tips/resources from the database
    tips_resources = TipResource.objects.filter().order_by('-created_at')
    return render(request, 'ecommerce/tipsandresources.html', {'tips_resources': tips_resources})

# Tip/Resource detail view
def tip_detail(request, slug):
    tip = get_object_or_404(TipResource, slug=slug)  # Fetch the tip/resource using its slug
    return render(request, 'ecommerce/tip_detail.html', {'tip': tip})

# About page view
def about_view(request):
    team_members = TeamMember.objects.all()
    return render(request, 'ecommerce/about.html', {'team_members': team_members})

# Contact page view
def contact(request):
    return render(request, 'ecommerce/contact.html')

# Cart page view
def cart(request):
    return render(request, 'ecommerce/cart.html')

