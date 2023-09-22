from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm


urlpatterns = [
    path("", views.hotel, name="hotel"),
    path("about/", views.about, name="about"),

    path('signup/', views.signin, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='hotel/sign_in.html', authentication_form=LoginForm),
         name='signin'),
    path('exit/', auth_views.LogoutView.as_view(next_page=''), name='exit'),
]