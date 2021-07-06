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

class HomePage(Page):
    """The start page of the Skill-DB site. 
    This page must NOT exist more than one time for the site.
    """

    max_count = 1

    profile_title = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)

    birth_date = models.DateField(null=True, blank=True)

    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Header background image',
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel("profile_title"),
        FieldPanel("first_name"),
        FieldPanel("last_name"),
        FieldPanel("birth_date"),
        ImageChooserPanel("profile_image"),
    ]

    @property 
    def full_name(self):
        return self.first_name + " " + self.last_name

class AboutPage(Page):
    """A customizable About page."""

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
