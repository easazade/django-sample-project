from django.contrib import admin
from jobs.models import Job

# Register your models here.
# the purpose of this page is to include our models here so we can show it in admin page

admin.site.register(Job)
