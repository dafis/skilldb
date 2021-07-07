from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import ( 
    FieldPanel, 
    FieldRowPanel, 
    InlinePanel, 
    MultiFieldPanel
)
from wagtail.images.edit_handlers import ( 
    ImageChooserPanel
)
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
)

class AboutPage(Page):
    """A customizable About page."""

    parent_page_types = [ 
        'profil.ProfilePage',
    ]

    content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("content", classname="full"),
    ]

class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
         on_delete = models.CASCADE,
         related_name = 'form_fields'
    )

class ContactPage(AbstractEmailForm):
    """ Page with a contact form and a recapture. """
    
    template = 'home/contact_page.html'
    parent_page_types = [ 
        'profil.ProfilePage',
    ]

    intro = RichTextField(blank = True)
    thank_you_text = RichTextField(blank = True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form Fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname = 'col-6'),
                FieldPanel('to_address', classname="col-6")
            ]),
            FieldPanel('subject'),
        ], heading = "Email Settings" )
    ]