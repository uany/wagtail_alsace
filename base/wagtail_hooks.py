from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from events.models import Event

class EventAdmin(ModelAdmin):
    menu_label = 'Events'
    menu_icon = 'fa-calendar'  # change as required
    menu_order = 222
    model = Event
    list_display = ('title', 'location_name', 'date')
    search_fields = ('title', 'location_name')
    ordering = ('-date',)

modeladmin_register(EventAdmin)
