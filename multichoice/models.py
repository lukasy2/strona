from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.db import models
from quiz.models import Question


ANSWER_ORDER_OPTIONS = (
    ('content', _('Content')),
    ('random', _('Random')),
    ('none', _('None'))
)


class MCQuestion(Question):

    answer_order = models.CharField(
        max_length=30, null=True, blank=True,
        choices=ANSWER_ORDER_OPTIONS,
        help_text=_("Kolejność w jakiej możliwe opcje "
                    "odpowiedzi są wyświetlane "
                    "użytkownikowi."),
        verbose_name=_("Kolejność odpowiedzi"))

    def check_if_correct(self, guess):
        answer = Answer.objects.get(id=guess)

        if answer.correct is True:
            return True
        else:
            return False

    def order_answers(self, queryset):
        if self.answer_order == 'content':
            return queryset.order_by('content')
        if self.answer_order == 'random':
            return queryset.order_by('?')
        if self.answer_order == 'none':
            return queryset.order_by()
        return queryset

    def get_answers(self):
        return self.order_answers(Answer.objects.filter(question=self))

    def get_answers_list(self):
        return [(answer.id, answer.content) for answer in
                self.order_answers(Answer.objects.filter(question=self))]

    def answer_choice_to_string(self, guess):
        return Answer.objects.get(id=guess).content

    class Meta:
        verbose_name = _("Pytanie testowe")
        verbose_name_plural = _("Pytania testowe")


@python_2_unicode_compatible
class Answer(models.Model):
    question = models.ForeignKey(MCQuestion, verbose_name=_("Pytanie"))

    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text=_("Wpisz tekst odpowiedzi, "
                                           "który ma zostać wyświetlony"),
                               verbose_name=_("Odpowiedzi"))

    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text=_("Czy to jest poprawna odpowiedź?"),
                                  verbose_name=_("Prawda"))

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Odpowiedź")
        verbose_name_plural = _("Odpowiedzi")
