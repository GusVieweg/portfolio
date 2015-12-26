from django.contrib import admin
from apps.research.models import Research


class ResearchAdmin(admin.ModelAdmin):
    """
    To avoid the need to create a custom backend when I want to create a new blog post,
    and to also bundle a means of making sure I'm the only one making these post changes,
    I've decided to use the Django Admin site.
    """
    list_display = ('title', 'last_modified', 'date_added')
    ordering = ('-date_added',)

admin.site.register(Research, ResearchAdmin)
