from django.db import models
from django.utils import timezone

from wagtail.admin.edit_handlers import (
    FieldPanel,
    RichTextFieldPanel
)

from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, PageManager, PageQuerySet, Orderable
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Event(models.Model, index.Indexed):
    """
    A Django model to store a specific event information.
    """
    title = models.TextField(
        help_text='Name of the event',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    body = RichTextField(verbose_name="Description", blank=True)
    date = models.DateTimeField()
    location_name = models.TextField(
        help_text='Name of the location',
        blank=True)
    location_address = models.TextField(
        help_text='Address of the location',
        blank=True)

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        RichTextFieldPanel('body'),
        FieldPanel('date'),
        FieldPanel('location_name'),
        FieldPanel('location_address'),
    ]

    search_fields = (
        index.SearchField('title', partial_match=True, boost=10),
        index.SearchField('body'),
        index.FilterField('location_name')
    )

    def __str__(self):
        return self.title


class EventPageQuerySet(PageQuerySet):
    def future(self):
        today = timezone.localtime(timezone.now()).date()
        return self.filter(event__date__gte=today)

EventPageManager = PageManager.from_queryset(EventPageQuerySet)


class EventPage(Page):
    """
    Detail view for a specific event
    """
    objects = EventPageManager()
    seo_description = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    seo_keywords = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    event = models.ForeignKey(
        'events.Event',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        SnippetChooserPanel('event'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('seo_description', classname="full"),
        FieldPanel('seo_keywords', classname="full"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('seo_description'),
        index.SearchField('seo_keywords'),
    ]

    parent_page_types = ['EventIndexPage']


class EventIndexPage(Page):
    """
    Index page for events
    """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and '
        '3000px.'
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
    ]

    # Can only have EventPage children
    subpage_types = ['EventPage']

    # Returns a queryset of EventPage objects that are live, that are direct
    # descendants of this index page with most recent first
    def get_events(self):
        return EventPage.objects.live().descendant_of(self).order_by('-date')

    # Allows child objects (e.g. EventPage objects) to be accessible via the
    # template. We use this on the HomePage to display child items of featured
    # content
    def children(self):
        return self.get_children().specific().live()

    # Returns the above to the get_context method that is used to populate the
    # template
    def get_context(self, request, *args, **kwargs):
        context = super(EventIndexPage, self).get_context(request)
        context['events'] = self.get_events()

        return context
