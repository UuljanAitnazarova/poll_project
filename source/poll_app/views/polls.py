from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render

from poll_app.models import Poll, Choice, Answer
from poll_app.forms import PollForm

class PollListView(ListView):
    model = Poll
    template_name = 'poll/list.html'
    context_object_name = 'polls'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

class PollChoicesView(ListView):
    template_name = 'poll/detail.html'
    context_object_name = 'choices'

    def get_queryset(self):
        self.poll = get_object_or_404(Poll, pk=self.kwargs['pk'])
        return Choice.objects.filter(poll=self.poll)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = self.poll
        context['counter'] = self.statistics()
        return context

    def statistics(self):
        counter = 0
        for i in self.poll.answers.all():
            counter += 1
        return counter


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll/create.html'

    def get_success_url(self):
        return reverse('poll_list')

class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/delete.html'
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_list')


class SelectAnswerView(TemplateView):
    template_name = 'answers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = get_object_or_404(Poll, pk=self.kwargs['pk'])
        return context


    def post(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs['pk'])
        try:
            option = get_object_or_404(Choice, pk=request.POST['action'])
            answer = Answer.objects.create(poll=poll, option=option)
        except:
            return redirect('select_answer', pk=self.kwargs['pk'])
        return redirect('poll_list')












