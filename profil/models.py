"""Profile related pages and information blocks."""

from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import ( 
    FieldPanel,
    InlinePanel,
    MultiFieldPanel, 
)
from wagtail.images.edit_handlers import ( 
    ImageChooserPanel,
)
from modelcluster.models import ParentalKey
from wagtail.snippets.models import register_snippet


class ProfileListingPage(Page):
    """The profile listing page page. This should only exists once."""

    max_count = 1
    parent_page_types = [ 
        'wagtailcore.Page',
    ]

class ProfilePage(Page):
    """A consultants profile page."""

    parent_page_types = [ 
        'wagtailcore.Page',
        'profil.ProfileListingPage',
    ]

    first_name = models.CharField("Vorname", max_length=100)
    last_name = models.CharField("Familienname", max_length=100)
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
        MultiFieldPanel([
            FieldPanel("first_name"),
            FieldPanel("last_name"),
            FieldPanel("birth_date"),
        ], heading="Personal Data"),
        ImageChooserPanel("profile_image"),
        InlinePanel('soft_skills', label="Soft Skills"),
        InlinePanel('educations', label="Ausbildung"),
        InlinePanel('employments', label="Anstellungen"),
        InlinePanel('trainings', label="Schulungen"),
        InlinePanel('certificates', label="Zertifikate"),
    ]

    @property 
    def full_name(self):
        return self.first_name + " " + self.last_name



class Education(models.Model):
    """Important educational phase."""
    name = models.CharField("Titel", max_length=100)
    provider = models.TextField("Schule/Hochschule", max_length=100)
    description = models.TextField("Beschreibung")
    from_date = models.DateField("Von")
    to_date = models.DateField("Bis")

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "educations",
    )

class Employment(models.Model):
    """Employment if applicable."""
    name = models.CharField("Titel", max_length=100)
    employer = models.TextField("Arbeitgeber", max_length=100)
    description = models.TextField("Beschreibung")

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "employments",
    )

class Training(models.Model):
    """Attended training and further self education."""
    name = models.CharField("Kurstitel", max_length=100)
    provider = models.CharField("Anbieter", max_length=100)
    description = models.TextField("Beschreibung")

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "trainings",
    )

class Certificate(models.Model):
    """Achieved certificate."""
    name = models.CharField("Titel", max_length=100)
    provider = models.CharField("Aussteller", max_length=100)
    description = models.TextField("Beschreibung")

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "certificates",
    )

@register_snippet
class SoftSkill(models.Model):
    """The name and a short description of soft skills."""
    name = models.CharField("Bezeichnung", max_length=100)
    description = models.TextField("Beschreibung")

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "soft_skills",
    )

