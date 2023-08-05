from django.contrib import admin
from .models import Freelancer, Client, Skill, CustomUser


# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')


admin.site.register([Freelancer, Client, Skill])
