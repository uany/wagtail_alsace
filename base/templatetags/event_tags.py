from django import template

from events.models import EventPage

register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/

@register.inclusion_tag('tags/events_grid.html', takes_context=True)
def events_grid(context):
    events = EventPage.objects.future().order_by('event__date')
    context['events'] = events
    return context
