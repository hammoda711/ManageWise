from django.contrib import admin

# Register your models here.
# accounts/admin.py
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('email', 'username')
