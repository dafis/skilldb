from django.db import models
from django.db.models.fields import SlugField
from wagtail.core.models import Orderable, Page
from wagtail.admin.edit_handlers import (
    FieldPanel
)
from wagtail.snippets.models import register_snippet


@register_snippet
class BlogCategory(models.Model):
    """ """
    name = models.CharField(max_length=100)
    slug = SlugField( 
        verbose_name="slug",
        allow_unicode=True,
        max_length=150,
        help_text="A slug used in blog posts for the category."
        )

    panels= [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]
    class Meta: # noqa
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ("name", )

class BlogListingPage(Page):
    """ """
    parent_page_types = [ 
        'profil.ProfilePage',
    ]

class BlogPostPage(Page):
    """ """
    parent_page_types = [ 
        'blog.BlogListingPage',
    ]

