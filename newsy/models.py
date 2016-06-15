from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User')
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

		
# class Kategoria(models.Model):
    # nazwa = models.CharField(max_length=200)

    # def publikuj(self):
        # self.data_opublikowania = timezone.now()
        # self.save()

    # def __str__(self):
        # return self.nazwa