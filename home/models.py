from django.db import models
from wagtail.core.models import Page

class HomePage(Page):
    """
    The start page of the Skill-DB site. Visitors who are not logged in
    are redirected to this page. This page must NOT exist more than one time for the site.
    """

    max_count = 1
    

