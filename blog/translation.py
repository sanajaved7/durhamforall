from .models import BlogPage, BlogIndexPage
from wagtail_modeltranslation.translator import WagtailTranslationOptions
from wagtail_modeltranslation.translation import register

@register(BlogPage)
class BlogPageTR(WagtailTranslationOptions):
    fields = (
        'intro',
        'body',
    )

@register(BlogIndexPage)
class BlogIndexPageTR(WagtailTranslationOptions):
    fields = (
        'intro',
    )
