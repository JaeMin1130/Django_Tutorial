import datetime
from django.utils import timezone
from django.db import models
from django.contrib import admin

"""
In our poll app, we’ll create two models: Question and Choice. 
A Question has a question and a publication date. 
A Choice has two fields: the text of the choice and a vote tally. 
Each Choice is associated with a Question.

"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # toString()
    def __str__(self):
        return self.question_text

    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # toString()
    def __str__(self):
        return self.choice_text
