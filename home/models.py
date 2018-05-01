from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock


class HomePage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('table', TableBlock(template='blocks/table.html')),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
