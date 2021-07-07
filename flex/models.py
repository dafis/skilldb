"""A flexible page"""

from django.db import models
from wagtail.core.models import Page, StreamField
from wagtail.admin.edit_handlers import FieldPanel

class FlexPage(Page):
    """This page type can be used to combine flexible pages."""

    template = "flex/flex_page.html"

    parent_page_types = [ 
        'profil.ProfilePage',
    ]

    subtitle = models.CharField(max_length = 100, null = True, blank = True)
    
    
    content_panels = Page.content_panels + [
        FieldPanel("subtitle")
    ]

    class Meta: # noqa
        verbose_name = "Flexible Page"
        verbose_name_plural = "Flexible Pages"
