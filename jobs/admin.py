from django.contrib import admin
from .models import job

# Register your models here.
# the purpose of this page is to include our models here so we can show it in admin page 
admin.site.register(job)
