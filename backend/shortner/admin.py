from django.contrib import admin

# Register your models here.
from .models import URL,Counter


admin.site.register(URL)
admin.site.register(Counter)