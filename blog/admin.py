from django.contrib import admin

from blog.models import Post
from blog.models import Comment

class PostAdmin(admin.ModelAdmin):
# title = models.CharField(max_length=100)
# text = models.TextField()
# slug = models.SlugField(max_length=60)
    list_display = ('id', 'title', 'slug', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)

class CommentAdmin(admin.ModelAdmin):
# post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
# text = models.TextField()
# allowed = models.BooleanField(default=True)
    list_display = ('id', 'post', 'allowed', 'date_created',)
    list_display_selected = list_display
    readonly_fields = ('date_created', 'date_last_modified',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

