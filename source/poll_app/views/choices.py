from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect

from poll_app.models import Choice, Poll
from poll_app.forms import ChoiceForm

class ChoiceCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choices/create.html'

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        form.save_m2m()
        return redirect(reverse('poll_detail', kwargs={'pk': poll.pk}))


class ChoiceUpdateView(UpdateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choices/update.html'
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choices/delete.html'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk':self.object.poll.pk})

