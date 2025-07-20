from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home_page'),
    path('logout/',views.user_login_view,name="logout"),
    path('login/',views.user_login_view,name="login"),
    path('register/',views.user_signup_view,name="register"),   
]
