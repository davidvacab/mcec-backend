from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _
from members.models import Profile, Church

User = get_user_model()

class ChurchInLine(admin.StackedInline):
    model = Church
    extra = 0

class ProfileInLine(admin.StackedInline):
    model = Profile
    extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInLine, ChurchInLine]
    list_display = ['full_name', 'username', 'email', 'last_login']
    list_filter = ['groups', 'is_staff','is_active', 'is_verified']
    list_per_page = 10
    search_fields = ['username__istartswith', 'email__istartswith']
    form = UserChangeForm
    
    @admin.display(description=_("full name"))
    def full_name(self, user:User):
        return f'{user.profile.first_name} {user.profile.last_name}'