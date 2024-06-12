from django.contrib import admin

from .models import Category, Genre, Title, Review, Comment


class TitleAdmin(admin.ModelAdmin):
    """Reorganize titles view in admin panel."""
    list_display = ('name', 'year', 'description', 'category')
    search_fields = ('name', 'year')
    list_filter = ('year',)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    """Reorganize reviews view in admin panel."""
    list_display = ('pk', 'title', 'text', 'author', 'score', 'pub_date')
    search_fields = ('text', 'author')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    """Reorganize comments view in admin panel."""
    list_display = ('pk', 'review', 'author', 'text', 'pub_date')
    search_fields = ('text', 'author')
    empty_value_display = '-пусто-'


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
