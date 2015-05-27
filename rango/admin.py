from django.contrib import admin
from rango.models import Category, Page, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Category', {'fields': ['category']}),
        ('URL', {'fields': ['url']}),
        ('Views', {'fields': ['views']}),
    ]
    list_display = ('title', 'category', 'url', 'views')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
