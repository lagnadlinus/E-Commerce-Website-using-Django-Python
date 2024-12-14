




from django.urls import path  # Importing path function to map the URLs to their respective views
from . import views  # Importing views module

app_name = 'users'  # Define the namespace

# We are going to define a URL pattern that maps the URL for the view
urlpatterns = [
    path('login/',views.sign_in, name='login'),
    path('logout/',views.sign_out, name='logout'),
    path('register/',views.sign_up, name='register'),
]
