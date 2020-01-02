from django.contrib import admin
from .models import *
# Register your models here

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'author', 'tags']}),
        ('Date information', {'fields': ['date_published'], 'classes': ['collapse']}),
    ]
.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)