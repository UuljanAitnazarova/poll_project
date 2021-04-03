from django import forms

from poll_app.models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['option']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['option']