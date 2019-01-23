from django.contrib import admin

from .models import Link
from .models import LinkClick
from .models import PersonDetail


class LinkAdmin(admin.ModelAdmin):
# title = models.CharField(max_length=30)
# url = models.URLField()
# svg = models.TextField()
    list_display = ('id', 'title', 'url', 'date_created',)
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


admin.site.register(Link, LinkAdmin)
admin.site.register(LinkClick, LinkClickAdmin)
admin.site.register(PersonDetail, PersonDetailAdmin)
