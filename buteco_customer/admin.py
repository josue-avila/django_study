from django.contrib import admin
from buteco_customer.models import ButecoCustomer


class ButecoCustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_doc', 'phone')


admin.site.register(ButecoCustomer, ButecoCustomerAdmin)
