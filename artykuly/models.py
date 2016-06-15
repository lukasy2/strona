from django.db import models
from django.utils import timezone

class Category(models.Model):
    tytul = models.CharField(max_length=200)
    data_utworzenia = models.DateTimeField(
            default=timezone.now)
    data_opublikowania = models.DateTimeField(
            blank=True, null=True)

    def publikuj(self):
        self.data_opublikowania = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul

class Article(models.Model):
    kategoria = models.ForeignKey('Category')
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    docfile = models.FileField(upload_to='static/%Y/%m/%d', blank=True, null=True)
    data_utworzenia = models.DateTimeField(
            default=timezone.now)
    data_opublikowania = models.DateTimeField(
            blank=True, null=True)

    def publikuj(self):
        self.data_opublikowania = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul
		
class Lekcja(models.Model):
    kurs = models.ForeignKey('Article')
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    docfile = models.FileField(upload_to='static/%Y/%m/%d', blank=True, null=True)
    data_utworzenia = models.DateTimeField(
            default=timezone.now)
    data_opublikowania = models.DateTimeField(
            blank=True, null=True)

    def publikuj(self):
        self.data_opublikowania = timezone.now()
        self.save()

    def __str__(self):
        return self.tytul