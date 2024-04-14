from django.shortcuts import render, redirect
from swiftapp.form import RegistrationForm, LoginForm, UserItemForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SwiftUser, UserItems
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        # Create a form that has request.POST
        form = RegistrationForm()
        if request.method == 'POST':

            form = RegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                firstname = form.cleaned_data.get('first_name')
                messages.success(request, f'Your Account has been created {firstname} ! Proceed to log in')
                return redirect('login')  # Redirect to the home page

        else:
            form = RegistrationForm()

        return render(request, 'register.html', {'form': form})


def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        context = {}
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')

                user = authenticate(request, email=email, password=password)

                if user is not None:
                    auth_login(request, user)
                    messages.success(request, f'Welcome {user.email}')
                    return redirect('dashboard')
            else:
                context['login_form']=form

            #form = LoginForm()
            context['login_form']=form
        return render(request,'login.html', context)


@login_required(login_url='/login')
def items(request):
    form = UserItemForm()

    if UserItems.objects.filter(user=request.user).exists():
        messages.success(request, f'You have already added items')
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserItemForm(request.POST)

        if form.is_valid():
            user_items = form.save(commit = False)
            user_items.user = request.user
            user_items.save()

            messages.success(request, f'Successfully submitted')
            return redirect('dashboard')
    else:
        form = UserItemForm()

    return render(request, 'items.html', {'form': form})


@login_required(login_url='/login')
def edit(request, id):
    if request.method == 'POST':
        user = UserItems.objects.get(pk=id)
        form = UserItemForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request,f'Your changes have been saved')
            return redirect('dashboard')
            return render(request, 'edit.html', {'form':form})

    else:
        user = UserItems.objects.get(pk=id)
        form = UserItemForm(instance=user)

    return render(request, 'edit.html', {'form':form})



@login_required(login_url="/login")
def dashboard(request):
    user_items = UserItems.objects.filter(user=request.user)

    return render(request,'dashboard.html', {'user_items': user_items})


def Logout(request):
    logout(request)
    messages.success(request, ('Woops! you have logged out bye 👋'))
    return redirect('login')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


@login_required(login_url='/login')
@user_passes_test(lambda user:user.is_superuser, login_url='/login')
def display(request):
    #if request.method == 'GET':
    useritems = UserItems.objects.all()
    return render(request,'display.html', {"useritems": useritems})



def bad_request(request, exception):
    return render(request,'400.html', status=400)


def permission_denied(request, exception):
    return render(request,'403.html', status=403)

def page_not_found(request, exception):
    return render(request,'404.html', status=404)

def server_error(request, exception):
    return render(request,'500.html', status=500)
