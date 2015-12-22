from django.contrib import admin
from apps.blog.models import Post

# To avoid the need to create a custom backend when I want to create a new blog post,
# and to also bundle a means of making sure I'm the only one making these post changes,
# I've decided to use the Django Admin site.
admin.site.register(Post)
