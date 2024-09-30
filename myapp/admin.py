from django.contrib import admin
from.models import Role,user_details,bank_details

# Register your models here.

class showRole(admin.ModelAdmin):
    list_display = ["u_name"]


admin.site.register(Role,showRole)

class showuser_details(admin.ModelAdmin):
    list_display = ["u_name","u_password","u_email","u_phone_no","u_type","u_status"]
admin.site.register(user_details,showuser_details)

class showbank_details(admin.ModelAdmin):
    list_display = ["u_id","b_name","digit_no","end_month","end_year"]

admin.site.register(bank_details,showbank_details)
