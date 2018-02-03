from .models import BlogPage
from wagtail_modeltranslation.translation import TranslationOptions
from wagtail_modeltranslation.translation import register

@register(BlogPage)
class BlogPageTR(TranslationOptions):
    fields = (
        'body',
    )
