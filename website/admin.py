from django.contrib import admin

from .models import Customer,Interaction,Lead


admin.site.register(Customer)
admin.site.register(Interaction)
admin.site.register(Lead)