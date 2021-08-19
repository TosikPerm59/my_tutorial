from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_change', 'parent_name')
    list_display_links = ('name',)
    search_fields = ('name', 'content')
    list_filter = ('date_of_change', 'parent_name')


admin.site.register(Article, ArticleAdmin)
