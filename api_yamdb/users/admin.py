from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    """Reorganize users view in admin panel."""
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
    )
    list_editable = ('role',)
    search_fields = ('username', 'email')
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
