# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-28 12:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoria', 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='progress',
            options={'verbose_name': 'Postęp użytkownika', 'verbose_name_plural': 'Postępy użytkowników'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['category'], 'verbose_name': 'Pytanie', 'verbose_name_plural': 'Pytania'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Test', 'verbose_name_plural': 'Testy'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Podkategoria', 'verbose_name_plural': 'Podkategorie'},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='progress',
            name='score',
            field=models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Wynik'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Category', verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.CharField(help_text='Wpisz tekst pytania, które ma zostać wyświetlone', max_length=1000, verbose_name='Pytanie'),
        ),
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, help_text='Wyjaśnienie, które pojawi się po tym jak użytkownik udzieli odpowiedzi.', max_length=2000, verbose_name='Wyjaśnienie'),
        ),
        migrations.AlterField(
            model_name='question',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Plik'),
        ),
        migrations.AlterField(
            model_name='question',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.SubCategory', verbose_name='Podkategoria'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answers_at_end',
            field=models.BooleanField(default=False, help_text='Prawidłowa odpowiedź NIE jest wyświetlona po każdym pytaniu. Odpowiedzi są wyświetlone na końcu.', verbose_name='Odpowiedzi na końcu'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Category', verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.TextField(blank=True, help_text='opis testu', verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='draft',
            field=models.BooleanField(default=False, help_text='Jeśli tak, test nie jest wyświetlany na liście i może być rozwiązany tylko przez użytkowników, którzy mają uprawnienia do edycji.', verbose_name='Szkic'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='exam_paper',
            field=models.BooleanField(default=False, help_text='Jeśli tak, wynik każdego podejścia do egzaminu będzie przechowywany. Potrzebne do oceniania.', verbose_name='Egzamin'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='fail_text',
            field=models.TextField(blank=True, help_text='Wyświetli się w przypadku niezaliczenia.', verbose_name='Tekst niepowodzenia'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='max_questions',
            field=models.PositiveIntegerField(blank=True, help_text='Liczba pytań w każdym podejściu', null=True, verbose_name='Ilość pytań'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='pass_mark',
            field=models.SmallIntegerField(blank=True, default=0, help_text='Procent wymagany do zaliczenia egzaminu.', validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Próg procentowy'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='random_order',
            field=models.BooleanField(default=False, help_text='Wyświetla pytania w losowej kolejności czy tak jak są ustawione?', verbose_name='Losowa kolejność'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='single_attempt',
            field=models.BooleanField(default=False, help_text='Jeśli tak, użytkownik może podejść do egzaminu tylko raz. Osoby niezalogowane nie mogą podejść do egzaminu.', verbose_name='Jedno podejście'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='success_text',
            field=models.TextField(blank=True, help_text='Wyświetli się w przypadku zaliczenia.', verbose_name='Tekst powodzenia'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='url',
            field=models.SlugField(help_text='Przyjazny użytkownikowi adres URL', max_length=60, verbose_name='Łatwy adres URL'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='current_score',
            field=models.IntegerField(verbose_name='Aktualny wynik'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Koniec'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_list',
            field=models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Lista pytań'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='question_order',
            field=models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Kolejność pytań'),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='user_answers',
            field=models.TextField(blank=True, default='{}', verbose_name='Odpowiedzi użytkownika'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Category', verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Podkategoria'),
        ),
    ]
