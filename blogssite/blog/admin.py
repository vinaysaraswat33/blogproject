from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('imgshow', 'title',  'url', 'add_date',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_id',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


