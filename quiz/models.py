from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    question = models.TextField()

    def __str__(self):
        return self.question

class Option(models.Model):
    question = models.ForeignKey(Question)
    option = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option
