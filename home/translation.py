from .models import HomePage
from wagtail_modeltranslation.translator import WagtailTranslationOptions
from wagtail_modeltranslation.translation import register

@register(HomePage)
class HomePageTR(WagtailTranslationOptions):
    fields = (
        'body',
    )
