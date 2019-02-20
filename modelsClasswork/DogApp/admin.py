# this code allows the website to actually run
from django.contrib import admin
from .models import Dog

# Register your models here.
admin.site.register(Dog)

