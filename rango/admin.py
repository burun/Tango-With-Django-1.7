from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Category', {'fields': ['category']}),
        ('URL', {'fields': ['url']}),
    ]
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
