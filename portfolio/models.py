from django.db import models
from wagtail.core.models import Page

class ProjectListingPage(Page):
    """ This page let the visitor explore project rreferences of the developer. 
    """

class ReferenceListingPage(Page):
    """This page let the visitor explore the developers references. 
    We plan to support the following reference types: Named Customers, 
    Contacts, Example Code, Project Reports and Blog Entries """

class ExplorerPage(Page):
    """This page let the visitor explore the developers skills. 
    The page is edited completely by the developer. The user can choose
    between several types of information: Skill Groups, Soft Skils, Development Skills, 
    Programming Languages, Frameworks, Tooling, Testing,  Documentation, ..."""
