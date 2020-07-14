from post.models import Post
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Your_name', 'Your_Post_title', 'Your_Post', 'image', 'id']}),
    ]


admin.site.register(Post, PostAdmin)
