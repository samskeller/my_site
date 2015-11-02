from django.contrib import admin

from person_details.models import LinkType
from person_details.models import Link
from person_details.models import LinkClick


class LinkTypeAdmin(admin.ModelAdmin):
# name = models.CharField(max_length=64)
    list_display = ('id', 'name', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)


class LinkAdmin(admin.ModelAdmin):
# link_type = models.ForeignKey(LinkType, on_delete=models.PROTECT)
# url = models.URLField()
# title = models.CharField(max_length=30)
# icon = models.ImageField(upload_to='link_icons/', blank=True, null=True)
    list_display = ('id', 'link_type', 'url', 'title', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)

class LinkClickAdmin(admin.ModelAdmin):
# link = models.ForeignKey(Link, on_delete=models.PROTECT)
    list_display = ('id', 'link', 'date_created',)
    list_selected_display = list_display
    readonly_fields = ('date_created', 'date_last_modified',)

admin.site.register(LinkType, LinkTypeAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(LinkClick, LinkClickAdmin)
