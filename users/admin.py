from django.contrib import admin

from users.models import Users
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_filter = ("id", "email")
    

