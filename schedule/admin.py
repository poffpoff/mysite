from django.contrib import admin
from schedule.models import Calendar, Event, MySpecialUser
# Register your models here.

class CalendarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Calendar, CalendarAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end')
    search_fields = ['title']
    date_hierarchy = 'start'

admin.site.register(Event, EventAdmin)

admin.site.register(MySpecialUser)