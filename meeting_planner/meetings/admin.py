from django.contrib import admin

from .models import Meeting, Room, Building


admin.site.register(Building)
admin.site.register(Meeting)
admin.site.register(Room)

