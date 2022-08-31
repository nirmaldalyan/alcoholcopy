from django.contrib import admin
from django.contrib import admin
from django.contrib.admin.sites import site
from database.models import enquiry
class enquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','phoneno','website','message')

admin.site.register(enquiry,enquiryAdmin)

# Register your models here.
