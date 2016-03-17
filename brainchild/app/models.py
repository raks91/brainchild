from __future__ import unicode_literals
from django.db import models


idea_catagories = ["Office", "Food", "Technical", "Hackathon", "Random"]
vote_types = ["Up", "Down"]


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name']


class Idea(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(User, models.PROTECT)
    content = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class IdeaVote(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    idea = models.ForeignKey(Idea, models.PROTECT)
    type = models.CharField(max_length=4, choices=zip(vote_types, vote_types))


class IdeaCategory(models.Model):
    idea = models.ForeignKey(Idea, models.PROTECT)
    name = models.CharField(max_length=25, choices=zip(idea_catagories, idea_catagories))


class Comment(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    date = models.DateField()
    idea = models.ForeignKey(Idea, models.PROTECT)
    content = models.TextField(max_length=5000, blank=True)


class CommentVote(models.Model):
    user = models.ForeignKey(User, models.PROTECT)
    comment = models.ForeignKey(Comment, models.PROTECT)
    type = models.CharField(max_length=4, choices=zip(vote_types, vote_types))
