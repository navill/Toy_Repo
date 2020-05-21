from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created', 'updated']


admin.site.register(Post, PostAdmin)
