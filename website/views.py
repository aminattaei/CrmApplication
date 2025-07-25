from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Customer,Interaction,Lead
from .forms import CustomerForm


@login_required(login_url="/login")
def home_view(request):
    # Render the home page
    customers = Customer.objects.all()
    leads = Lead.objects.all()
    interactions = Interaction.objects.all()
    return render(request,"Index/index.html",{'customers':customers,'leads':leads,'interactions':interactions})

def user_logout_view(request):
    # Log the user out and show a success message
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect("home_page")


def user_signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create and log in the user
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully signed up and logged in!")
            return redirect("home_page")
        else:
            # Display an error if form is invalid
            messages.error(request, "The fields are not valid. Please check and try again.")
    else:
        # Display empty signup form
        form = UserCreationForm()

    return render(request, "registration/signup.html", {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate and log in the user
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home_page")
        else:
            # Invalid login credentials
            messages.error(request, "Invalid username or password.")
    else:
        # Display empty login form
        form = AuthenticationForm()

    return render(request, "registration/login.html", {'form': form})


# <-------------------------- Customer Classes -------------------------->

class CustomerUpdateView(generic.UpdateView):
    model = Customer
    context_object_name='customer'
    template_name = "Customer/customer_details.html"
    fields = ('full_name','email','phone','company','address','notes')

    def form_valid(self, form):
        form.save()
        messages.success(self.request,"Information changed successfully.")
        return redirect("home_page")
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request,"Customer Form not valid...! please check fields or send problem to support team.")
        return redirect("home_page")
    
class CustomerCreateView(generic.CreateView):
    """
    Create new customer information
    """
    model = Customer
    fields = ('full_name','email','phone','company','address','notes')
    template_name = "Customer/customer_create.html"

class CustomerDeleteView(generic.DeleteView):
    """
    Delete One Customer
    """
    model = Customer
    template_name = "Customer/customer_confirm_delete.html"
    success_url=reverse_lazy('home_page')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Customer successfully removed.")
        return super().delete(request, *args, **kwargs)

# <-------------------------- Lead Classes -------------------------->

class LeadUpdateView(generic.UpdateView):
    """
    Update One Lead Field
    """
    model = Lead
    context_object_name='lead'
    template_name = "Lead/lead_details.html"
    fields = ('full_name','email','phone','source','status')

    def form_valid(self, form):
        form.save()
        messages.success(self.request,"Information changed successfully.")
        return redirect("home_page")
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request,"Lead Form not valid...! please check fields or send problem to support team.")
        return redirect("home_page")

class LeadCreateView(generic.CreateView):
    """
    Create new Lead information
    """
    model = Lead
    fields = ('full_name','email','phone','source','status')
    template_name = "Lead/lead_create.html"

class LeadDeleteView(generic.DeleteView):
    """
    Delete One Lead
    """
    model = Lead
    template_name = "Lead/lead_confirm_delete.html"
    success_url=reverse_lazy('home_page')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Lead successfully removed.")
        return super().delete(request, *args, **kwargs)
    
# <-------------------------- Interaction Classes -------------------------->

# class InteractionUpdateView(generic.UpdateView):
#     """
#     Update One Interaction Field
#     """
#     model = Interaction
#     context_object_name='interaction'
#     template_name = "Interaction/interaction_details.html"
#     fields = ('__all__')

#     def form_valid(self, form):
#         form.save()
#         messages.success(self.request,"Information changed successfully.")
#         return redirect("home_page")
    
#     def form_invalid(self, form):
#         response = super().form_invalid(form)
#         messages.error(self.request,"Interaction Form not valid...! please check fields or send problem to support team.")
#         return redirect("home_page")

class InteractionDetailView(generic.DetailView):
    model = Interaction
    context_object_name='interaction'
    template_name = "Interaction/interaction_details.html"


class InteractionCreateView(generic.CreateView):
    """
    Create new Interaction information
    """
    model = Interaction
    fields = ('__all__')
    template_name = "Interaction/interaction_create.html"


class InteractionDeleteView(generic.DeleteView):
    """
    Delete One Interaction
    """
    model = Interaction
    template_name = "Interaction/interaction_confirm_delete.html"
    success_url=reverse_lazy('home_page')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Interaction successfully removed.")
        return super().delete(request, *args, **kwargs)