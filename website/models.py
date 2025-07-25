from django.db import models
from django.urls import reverse

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})
        
    


class Lead(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    source = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('new', 'جدید'),
        ('contacted', 'تماس گرفته شده'),
        ('converted', 'تبدیل شده به مشتری'),
        ('lost', 'از دست رفته'),
    ], default='new')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse("Lead_detail", kwargs={"pk": self.pk})


class Interaction(models.Model):
    contact_date = models.DateTimeField()
    summary = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.customer:
            name = self.customer.full_name
        elif self.lead:
            name = self.lead.full_name
        else:
            name = "Unknown"
        return f"{name} - {self.contact_date.strftime('%Y-%m-%d')}"


    def get_absolute_url(self):
        return reverse("Interaction_detail", kwargs={"pk": self.pk})