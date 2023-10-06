from django.contrib import admin
from .models import Post


# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'auth', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'auth']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['auth']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']