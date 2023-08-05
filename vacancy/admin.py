from django.contrib import admin
from .models import Vacancy, Tag

# Register your models here.

admin.site.register([Vacancy, Tag])