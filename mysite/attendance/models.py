from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(
        max_length=255,
    )


class Statistics(models.Model):
    gpa = models.IntegerField()


class Subject(models.Model):
    subject = models.CharField(
        max_length=255,
    )


class Score(models.Model):
    score = models.CharField(
        max_length=3,
    )
