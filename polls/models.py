from django.db import models
from mezzanine.pages.models import Page

# The members of Page will be inherited by the Poll
# model, such as title, slug, etc. For polls we can use
# the title field to store the poll's question. For our
# model  definition, we just add any extra fields that
# aren't part of the Page model, in this case, date of
# publication.


class Poll(Page):
    # question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")


class Choice(models.Model):
    poll = models.ForeignKey("Poll")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
