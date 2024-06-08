from django.contrib import admin

from .models import Category, Genre, Title


class TitleAdmin(admin.ModelAdmin):
    """Reorganize titles view in admin panel."""
    list_display = ('name', 'year', 'description', 'category')
    search_fields = ('name', 'year')
    list_filter = ('year',)
    empty_value_display = '-пусто-'


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title, TitleAdmin)
