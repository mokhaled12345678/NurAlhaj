from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Packages, Gallery, Bookings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm, BookingForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        data = {'name':name,
                'email':email,
                'subject':subject,
                "message":message}

        message = '''
                New Message: {}


                From: {}
                '''.format(data['message'], data['email'])
        # Send email
        send_mail(data['subject'], message, '', ['mohammedkhaledmali888@gmail.com'])

    packages = Packages.objects.all()
    gallery = Gallery.objects.all()
    return render(request, 'UserView/index.html', {'packages': packages, 'gallery': gallery})
def get_packages(request):
    packages = Packages.objects.all()
    response = [
        {
            'name':package.name,
            'image': package.image.url,
            'location': package.get_title(),
            'description': package.description,
            'last_price': package.get_price(),
            'price':package.get_sale_price(),
            'avilable' : package.available_counter,
            'plane':package.get_plane(),
        }
        for package in packages
    ]
    return JsonResponse(response, safe=False)

def login_user(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            authenticated_user = authenticate(request, username=email, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')
            else:
                messages.error(request, "Incorrect password")
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
    
    return render(request, 'UserView/login-register.html', {'page': page,  'messages': messages.get_messages(request)})

def logoutUser(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']  # Add this line to get the username
            phone = form.cleaned_data['phone_number']
            # Use the custom user model manager to create the user
            User = get_user_model()  # Get the custom user model
            user = User.objects.create_user(username=username, phone_number=phone, email=email, password=password)  # Pass the username
            
            # Authenticate and login the user
            authenticated_user = authenticate(request, username=email, password=password)  # Pass the username
            print(authenticated_user)
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('home')  # Redirect to the 'home' URL
    else:
        form = NewUserForm()

    return render(request, 'UserView/login-register.html', {'form': form})

@login_required(login_url='login')
def booking(request, location):
    packagename = location #Packages.objects.filter(location__name=location).first().name  # Filter by location name
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']  # Use title instead of location
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                error_message = "User does not exist. Please enter a valid username."
                return render(request, 'UserView/booking.html', {'message': error_message,
                                                                'form': form,
                                                                'packagename':packagename})
            
            package = Packages.objects.filter(name=title).first()  # Filter by location name
            # Check if a booking with the same user and package already exists
            if Bookings.objects.filter(user=user, package=package).exists():
                error_message = "Booking already exists. Please try again."
                return render(request, 'UserView/booking.html', {'message': error_message,
                                                                'form': form,
                                                                'packagename':packagename})
            
            if package and package.available_counter > 0:
                Bookings.objects.create(user=user, package=package)
                package.available_counter -= 1
                package.save()
                redirect_url = reverse('homePay', args=[package.name, package.location.name])
                return redirect(redirect_url)  # Replace 'home' with your success page URL
            
            error_message = "Package is not available. Please select a valid package."
            return render(request, 'UserView/booking.html', {'message': error_message,
                                                                'form': form,
                                                                'packagename':packagename})
    
    else:
        form = BookingForm()
    
    return render(request, 'UserView/booking.html', {'form': form,
                                                    'packagename':packagename})