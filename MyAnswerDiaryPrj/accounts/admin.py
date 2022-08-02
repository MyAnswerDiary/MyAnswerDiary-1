from django.contrib import admin
from .models import UserModel

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_pw',
        'user_name'
    )