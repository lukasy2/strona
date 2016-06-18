from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.db import models
from quiz.models import Question


class TF_Question(Question):
    correct = models.BooleanField(blank=False,
                                  default=False,
                                  help_text=_("Zaznacz jeśli odpowiedź jest "
                                              "prawdziwa. Zostaw pole puste jeśli jest"
                                              " fałszywa."),
                                  verbose_name=_("Prawda"))

    def check_if_correct(self, guess):
        if guess == "True":
            guess_bool = True
        elif guess == "False":
            guess_bool = False
        else:
            return False

        if guess_bool == self.correct:
            return True
        else:
            return False

    def get_answers(self):
        return [{'correct': self.check_if_correct("True"),
                 'content': 'True'},
                {'correct': self.check_if_correct("False"),
                 'content': 'False'}]

    def get_answers_list(self):
        return [(True, True), (False, False)]

    def answer_choice_to_string(self, guess):
        return str(guess)

    class Meta:
        verbose_name = _("Pytanie prawda/fałsz")
        verbose_name_plural = _("Pytania prawda/fałsz")
        ordering = ['category']
