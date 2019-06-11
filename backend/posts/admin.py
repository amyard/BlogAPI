from django.contrib import admin
from backend.posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author',)
    list_display_links = ('title', )
    search_fields = ['author', 'title']
    list_filter = ('created',)
    date_hierarchy = ('created')
    prepopulated_fields = {'slug': ('title',)}