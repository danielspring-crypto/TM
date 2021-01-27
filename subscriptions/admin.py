from django.contrib import admin
from subscriptions.models import StripeCustomer
from .models import New

admin.site.register(New)

admin.site.register(StripeCustomer)