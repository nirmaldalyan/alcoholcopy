from django.contrib import admin
from django.contrib.admin.sites import site
from first.models import first
class firstAdmin(admin.ModelAdmin):
    list_display=('first_title','icon','service_des')

admin.site.register(first,firstAdmin)

# Register your models here.
