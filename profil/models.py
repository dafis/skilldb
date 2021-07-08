"""Profile related pages and information blocks."""

from django.utils.translation import gettext_lazy as _

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

    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    birth_date = models.DateField(_("Birth Date"), null=True, blank=True)

    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False, null=True,
        related_name='+',
        help_text=_('Profile Image'),
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("first_name"),
            FieldPanel("last_name"),
            FieldPanel("birth_date"),
        ], heading=_("Personal Data")),
        ImageChooserPanel("profile_image"),
        InlinePanel('soft_skills', label=_("Soft Skills")),
        InlinePanel('educations', label=_("Education")),
        InlinePanel('employments', label=_("Employments")),
        InlinePanel('trainings', label=("Trainings")),
        InlinePanel('certificates', label=_("Certificates")),
    ]

    @property 
    def full_name(self):
        return self.first_name + " " + self.last_name


class Education(models.Model):
    """Important educational phase."""
    name = models.CharField(_("Title"), max_length=100)
    provider = models.TextField(_("Institution"), max_length=100)
    description = models.TextField(_("Description"))
    from_date = models.DateField(_("From"))
    to_date = models.DateField(_("To"))

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "educations",
    )

class Employment(models.Model):
    """Employment if applicable."""
    name = models.CharField("Title", max_length=100)
    employer = models.TextField(_("Employer"), max_length=100)
    description = models.TextField(_("Description"))

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "employments",
    )

class Training(models.Model):
    """Attended training and further self education."""
    name = models.CharField(_("Title"), max_length=100)
    provider = models.CharField(_("Provider"), max_length=100)
    description = models.TextField(_("Description"))

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "trainings",
    )

class Certificate(models.Model):
    """Achieved certificate."""
    name = models.CharField(_("Title"), max_length=100)
    provider = models.CharField(_("Institution"), max_length=100)
    description = models.TextField(_("Description"))

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "certificates",
    )

@register_snippet
class SoftSkill(models.Model):
    """The name and a short description of soft skills."""
    name = models.CharField(_("Name"), max_length=100)

    profile = ParentalKey(
        "profil.ProfilePage", 
        related_name = "soft_skills",
    )

