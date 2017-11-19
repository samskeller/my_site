from django.contrib import admin

from .models import LinkType
from .models import Link
from .models import LinkClick
from .models import PersonDetail


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

class PersonDetailAdmin(admin.ModelAdmin):
# detail_type = models.CharField(max_length=40, unique=True)
# detail_value = models.TextField()
    list_display = ('id', 'detail_type', 'date_created',)
    list_selected_display = list_display
    readonly_field = ('date_created', 'date_last_modified',)


admin.site.register(LinkType, LinkTypeAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(LinkClick, LinkClickAdmin)
admin.site.register(PersonDetail, PersonDetailAdmin)
