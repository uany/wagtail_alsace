from django.db import models
from django.utils import timezone

from wagtail.admin.edit_handlers import (
    FieldPanel,
    RichTextFieldPanel
)

from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.models import Page, PageManager, PageQuerySet

class EventPageQuerySet(PageQuerySet):
    def future(self):
        today = timezone.localtime(timezone.now()).date()
        return self.filter(date__gte=today)

EventPageManager = PageManager.from_queryset(EventPageQuerySet)

class EventPage(Page):
    """
    Detail view for a specific event
    """
    objects = EventPageManager()
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    body = RichTextField(verbose_name="Page body", blank=True)
    date = models.DateTimeField()

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('date', classname="full"),
        RichTextFieldPanel('body')
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
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
