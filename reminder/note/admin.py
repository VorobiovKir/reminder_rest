from django.contrib import admin

from .models import Colors, Categories, Tags, Notes, Images

admin.site.register(Notes)
admin.site.register(Categories)
admin.site.register(Colors)
admin.site.register(Tags)
admin.site.register(Images)
