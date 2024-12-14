


from django.shortcuts import render, redirect
from .forms import LoginForm  # Assuming you've created a LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm 


# creating views from  here 
def sign_in(request):
    """
    Handles user login functionality. Displays a login form and processes login credentials.
    If the user is already authenticated, they are redirected to the homepage.
    """
    # Check if the user is already authenticated
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('homepage')  # Redirect to the homepage if logged in
        # Show the login form for non-authenticated users
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    # Process login for POST requests
    elif request.method == 'POST':
        form = LoginForm(request.POST)  # Use your LoginForm for validation

        if form.is_valid():
            # Extract credentials from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, "Successfully logged in!")
                return redirect('homepage')  # Redirect to the homepage
            else:
                # Authentication failed
                messages.error(request, "Invalid username or password.")
        else:
            # Form validation failed; add error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

        # Re-render the login page with form errors
        return render(request, 'users/login.html', {'form': form})
    

def sign_out(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('users:login')  # Redirect to login page


def sign_up(request):
    if request.method == 'GET':  # Display the registration form
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
    elif request.method == 'POST':  # Handle form submission
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create the user but don't save yet
            user.username = user.username.lower()  # Ensure username is lowercase
            user.save()  # Save the user to the database

            login(request, user)  # Log the user in
            messages.success(request, "Registration successful!")
            return redirect('homepage')  # Redirect to the homepage
        else:
            # Form is not valid: re-render the form with error messages
            messages.error(request, "Please correct the errors below.")
            return render(request, 'users/register.html', {'form': form})
    
    # Fallback: If request method is neither GET nor POST, return an error response
    return render(request, 'users/register.html', {'form': RegisterForm()})






    

    