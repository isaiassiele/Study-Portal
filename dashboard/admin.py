from django.contrib import admin
from . models import *

# Register your models here.

class StaffAdmin(admin.AdminSite):
    site_header = "Accounts admin"
    site_title = "Acoounts Admin Portal"
    index_title = "Welcome to accounts managements"

staff_admin_site = StaffAdmin(name='staff_admin')

staff_admin_site.register(User)
admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)