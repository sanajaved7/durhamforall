from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class BlogPage(Page):
    full_width = models.BooleanField("Show this post as full-width (no sidebar)?", default=False)
    body = RichTextField(blank=True)

    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('html', blocks.RawHTMLBlock())
    ])

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('full_width'),
    ]
