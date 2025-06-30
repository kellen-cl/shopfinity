from django.contrib import admin
from.models import User

# Register your models here.
@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',)
    search_fields = ('username', 'email')
    ordering=('username',)
    list_filter = ('is_active', 'is_staff', )
