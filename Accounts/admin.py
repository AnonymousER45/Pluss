from django.contrib import admin
from . models import Customer, Address,OTP,OTPmail,Pincode,Coupon,Attendance
from .forms import CustomerCreationForm
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput
from django.db import models

class CustomerAdmin(UserAdmin):
    model = Customer
    add_form = CustomerCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Customer Phone Number',
            {
                'fields': (
                    'phone_number',
                )
            }
        )
    )

    list_display = ['id', 'username', 'first_name', 'last_name',
                    'phone_number', 'email', 'is_staff', 'is_superuser','pincode' ]
    search_fields = ('email', 'username')
    ordering = ('email',)
    list_filter = ['groups',]
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size':'20'})},
    }


"""
class CustomerAdmin(UserAdmin):
    model = Customer
    add_form = CustomerCreationForm
    list_display = ['email', 'username', 'phone_number']
    add_fieldsets = (
        (None, {'fields': ('email', 'username',  'phone_number','password')}),
    )
    fieldsets = (
        (None, {
            "fields": (
                ('email','password', 'username', 'phone_number', 'is_staff', 'is_superuser','groups' )

            ),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    list_filter = ['groups',]
    formfield_overrides = {
        models.IntegerField: {'widget': TextInput(attrs={'size':'20'})},
    }
 """

class AddressAdmin(admin.ModelAdmin):
    list_display = ("id","customer_id", "name","city","line1","line2","line3","addtype","addpincode")
    list_filter = ['addtype','addpincode','city']


class AttendanceAdmin(admin.ModelAdmin):
    emp_id = Customer.objects.filter(is_staff=True)
    list_filter = ['date','emp_id']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(OTP)
admin.site.register(OTPmail)
admin.site.register(Pincode)
admin.site.register(Coupon)



