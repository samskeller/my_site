from django.contrib import admin

from person_details.models import Link
from person_details.models import LinkClick


class LinkAdmin(admin.ModelAdmin):
# url = models.URLField()
# title = models.CharField(max_length=30)
# icon = models.ImageField(upload_to='link_icons/', blank=True, null=True)
    list_display = ('id', 'url', 'title', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)

class LinkClickAdmin(admin.ModelAdmin):
# link = models.ForeignKey(Link, on_delete=models.PROTECT)
    list_display = ('id', 'link', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)

admin.site.register(Link, LinkAdmin)
admin.site.register(LinkClick, LinkClickAdmin)
