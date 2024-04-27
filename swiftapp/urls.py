from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name='home'),
    path("register/", views.register, name="register"),
    path("login/", views.Login, name="login"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("about/", views.about, name="about"),
    path("logout/", views.Logout, name="logout"),

    path("display/", views.display, name="display"),
    path('items/', views.items, name="items"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('export-excel', views.export_excel, name="export-excel"),
    path('toggle_display', views.toggle_display, name="toggle_display"),

    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),

    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
]
