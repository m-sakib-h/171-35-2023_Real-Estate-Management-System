from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages, auth   # jei view te kaj korbo seikhana import korbo
from django.contrib.auth.models import User
from listings.models import Listing, Inquiry
# Create your views here.
from django.urls import reverse


def registration(request):
    if request.method == "POST":
        # print(request.POST)
        method_dict = request.POST.copy()
        first_name = method_dict.get('first_name')
        last_name = method_dict.get('last_name')
        username = method_dict.get('username')
        email = method_dict.get('email')
        password = method_dict.get('password')
        password2 = method_dict.get('password2')
        if password == password2:
            # messages.error(request, 'password not match')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exist!')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exist!')
                else:
                    # messages.error(request, 'You are eligible for Register')
                    # User Create
                    User.objects.create_user(username=username,
                                             password=password,
                                             first_name=first_name,
                                             last_name=last_name,
                                             email=email)
                    messages.success(request, 'You are successfully registered')
                    return HttpResponseRedirect(reverse('login'))
                    # return redirect('login')    # Not Standard
        else:
            messages.error(request, 'Password does not match')
             # messages.error(request, 'Testing Error Message!')

        return HttpResponseRedirect(reverse('registration'))

        # return redirect("registration") #not standard
        # return HttpResponseRedirect(reversed('user-register'))    #Standard
        # print(request.POST)

    return render(request, 'accounts/registration.html')


def login(request):
    if request.method == "POST":
        # print(request.POST)
        method_dict = request.POST.copy()
        username = method_dict.get('username')
        password = method_dict.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are successfully logged in')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, ' Invalid username and password')
            return HttpResponseRedirect(reverse('login'))
            # return HttpResponseRedirect(reversed('user-login')) #Standard
            # return redirect('user-login')  # Not Standard
            # print(request.POST)

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return HttpResponseRedirect(reverse('home'))


def dashboard(request):
    inquiry_list = Inquiry.objects.all()            # latest = Listing.objects.order_by('-list_date')[:3]   # Suppose 3 listing
                                                    # listing_list = Inquiry.objects.all()  # [:1]    # Suppose 6 listing
    context = {
        'latest': inquiry_list,
    }
    return render(request, 'accounts/dashboard.html',context)
