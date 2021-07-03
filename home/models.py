from django.db import models
from wagtail.core.models import Page

class HomePage(Page):
    """
    The start page of the Skill-DB site. 
    This page must only exist one time for the site.
    """

    max_count = 1
    

class OverviewPage(Page):
    """
    Overview pages are used to list profile pages.
    """

class ProfilePage(Page):
    """
    Profile Pages are used to manage developer, consultant ond prospective customer 
    profiles.
    """

class ExplorerPage(Page):
    """
    Find profiles in terms of skills, knowledge 
    and projects by required" or optional feastures.
    """



