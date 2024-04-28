from django.shortcuts import render, redirect
from swiftapp.form import RegistrationForm, LoginForm, UserItemForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import SwiftUser, UserItems
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
import datetime
import xlwt
#from .models import ShowElement


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

    #if UserItems.objects.filter(user=request.user).exists():
        #messages.success(request, f'You have already added items')
        #return redirect('dashboard')

    if request.method == 'POST':
        form = UserItemForm(request.POST)

        if form.is_valid():
            user_items = form.save(commit = False)

            for field_name, choices in request.POST.user_items():
                if field_name not in form.fields:
                    form.set_dynamic_choices(field_name, choices)
                    setattr(user_items, field_name, request.POST[field_name])
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


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=UserItems' + str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('UserItems')
    row_num = 0

    columns = [
        "Name", "Garri(white-Ijebu)", "Garri(white-Bendel)","Garri(yellow)","Rice(Nig)","Rice(foreign-small-grain)","Rice(foreign-big-grain)","Beans(honey)",
        "Beans(drum)","Beans(pelebe)","Onions(big-size)","Onions(gen-size)","Spag(auntyB)","Spag(Gpenny)","Spag(crown)","Spag(dangote)",
        "Noodles(indomie-oriental)","Noodles(indomie-chicken)","Noodles(chikki-chicken)","Noodles(mimee-chicken)","Yam","Red-oil",
        "Veg-oil","Satchet-tomatoe","Tin-tomatoe(220g)","Tin-tomatoe(450g)","Semo"
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for column in range(len(columns)):
        ws.write(row_num, column, columns[column], font_style)

    font_style = xlwt.XFStyle()

    useritems = UserItems.objects.all()

    for user in useritems:
        row_num += 1
        ws.write(row_num, 0, user.user.first_name, font_style)
        ws.write(row_num, 1, user.white_garri_ijebu, font_style)
        ws.write(row_num, 2, user.white_garri_bendel, font_style)
        ws.write(row_num, 3, user.yellow_garri, font_style)
        ws.write(row_num, 4, user.nig_rice, font_style)
        ws.write(row_num, 5, user.foreign_rice_small_grain, font_style)
        ws.write(row_num, 6, user.foreign_rice_big_grain, font_style)
        ws.write(row_num, 7, user.honey_beans, font_style)
        ws.write(row_num, 8, user.drum_beans, font_style)
        ws.write(row_num, 9, user.pelebe_beans, font_style)
        ws.write(row_num, 10, user.onions_big_size, font_style)
        ws.write(row_num, 11, user.onions_gen_size, font_style)
        ws.write(row_num, 12, user.aunty_b_spag, font_style)
        ws.write(row_num, 13, user.g_penny_spag, font_style)
        ws.write(row_num, 14, user.crown_spag, font_style)
        ws.write(row_num, 15, user.dangote_spag, font_style)
        ws.write(row_num, 16, user.indomie_oriental, font_style)
        ws.write(row_num, 17, user.indomie_chicken, font_style)
        ws.write(row_num, 18, user.chikki_noodles, font_style)
        ws.write(row_num, 19, user.mimee_noodles, font_style)
        ws.write(row_num, 20, user.yam_tubers, font_style)
        ws.write(row_num, 21, user.red_oil, font_style)
        ws.write(row_num, 22, user.veg_oil,font_style)
        ws.write(row_num, 23, user.satchet_tomatoe, font_style)
        ws.write(row_num, 24, user.tin_tomatoe_220g, font_style)
        ws.write(row_num, 25, user.tin_tomatoe_450g, font_style)
        ws.write(row_num, 26, user.semo, font_style)

    wb.save(response)
    return response




def bad_request(request, exception):
    return render(request,'400.html', status=400)


def permission_denied(request, exception):
    return render(request,'403.html', status=403)

def page_not_found(request, exception):
    return render(request,'404.html', status=404)

def server_error(request, exception):
    return render(request,'500.html', status=500)
