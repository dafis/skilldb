from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    """The start page of the Skill-DB site. This page is must only exist one time for the site."""
    max_count=1

class DeveloperPage(Page):
    pass