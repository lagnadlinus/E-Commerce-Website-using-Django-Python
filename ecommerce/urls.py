


from django.urls import path  # Importing path function to map the URLs to their respective views
from . import views  # Importing views module

# We are going to define a URL pattern that maps the URL for the view
urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage route
    path('products/', views.products, name='products'),  # Products page route
    path('tipsandresources/', views.tipsandresources, name='tipsandresources'),  # Tips and resources page
    path('about/', views.about_view, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('cart/', views.cart, name='cart'),  # Cart page

    # route for product detail view
    path('product-detail/<slug:slug>/', views.product_detail, name='product-detail'),

    # route for Tip/resource detail view
    path('tipsandresources/<slug:slug>/', views.tip_detail, name='tip-detail'),
]
