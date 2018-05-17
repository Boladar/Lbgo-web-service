from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    question_id = models.AutoField(primary_key = True)
    content = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.content

class Anwser(models.Model):
    question_id = models.IntegerField()
    content = models.CharField(max_length = 1000, blank=True, null=True)

class Objective(models.Model):
    name = models.CharField(max_length= 100,primary_key=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    questions = models.ManyToManyField(Question, related_name='questions')
    event = models.ForeignKey('Event',on_delete=models.PROTECT, blank=True, null=True)

class Team(models.Model):
    owner = models.ForeignKey(User,on_delete=models.PROTECT)
    name = models.CharField(max_length=100, primary_key=True)
    members = models.ManyToManyField(User,related_name='members')
    visitedObjectives = models.ManyToManyField(Objective, related_name='visitedObjectives')
    

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    startTime = models.DateTimeField(blank=True, null=True)
    endTime = models.DateTimeField(blank=True, null=True)
    teams = models.ManyToManyField(Team,related_name='teams')
    objectives = models.ManyToManyField(Objective,related_name='objectives')

    def __str__(self):
        return self.name