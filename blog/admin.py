from django.contrib import admin
from .models import *
# Register your models here

class BlogAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['title', 'author']}),
    #     ('Date information', {'fields': ['date_published'], 'classes': ['collapse']}),
    #     ('Others', {'fields': ['tags']})
    # ]
    list_display = ('title', 'author', 'date_published', 'was_published_recently')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)