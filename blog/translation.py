from .models import BlogPage, BlogIndexPage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.translation import register

@register(BlogPage)
class BlogPageTR(TranslationOptions):
    fields = (
        'intro',
        'body',
    )

@register(BlogIndexPage)
class BlogIndexPageTR(TranslationOptions):
    fields = (
        'intro',
    )
