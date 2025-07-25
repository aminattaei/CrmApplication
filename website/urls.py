from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='home_page'),
    path('logout/',views.user_login_view,name="logout"),
    path('login/',views.user_login_view,name="login"),
    path('register/',views.user_signup_view,name="signup"),     
    # <---- Customers Urls ---->
    path('customer/<int:pk>/',views.CustomerUpdateView.as_view(),name="Customer_detail"),
    path('customer/create/',views.CustomerCreateView.as_view(),name="customer_create"),
    path('customer/<int:pk>/delete/',views.CustomerDeleteView.as_view(), name='customer_delete'),
    # <---- Customers Urls ---->
    path('lead/<int:pk>/',views.LeadUpdateView.as_view(),name="Lead_detail"),
    path('lead/create/',views.LeadCreateView.as_view(),name="lead_create"),
    path('lead/<int:pk>/delete/',views.LeadDeleteView.as_view(), name='lead_delete'),
    # <---- Intercation Urls ---->
    path('interaction/<int:pk>/',views.InteractionDetailView.as_view(),name="Interaction_detail"),
    path('interaction/create/',views.InteractionCreateView.as_view(),name="interaction_create"),
    path('interaction/<int:pk>/delete/',views.InteractionDeleteView.as_view(), name='interaction_delete'),
    

]
