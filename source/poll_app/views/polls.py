from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import get_object_or_404

from poll_app.models import Poll, Choice
from poll_app.forms import PollForm

class PollListView(ListView):
    model = Poll
    template_name = 'poll/list.html'
    context_object_name = 'polls'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

# class PollDetailView(DetailView):
#     model = Poll
#     template_name = 'poll/detail.html'
#     context_object_name = 'poll'

class PollChoicesView(ListView):
    template_name = 'poll/detail.html'
    context_object_name = 'choices'

    def get_queryset(self):
        self.poll = get_object_or_404(Poll, pk=self.kwargs['pk'])
        return Choice.objects.filter(poll=self.poll)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poll'] = self.poll
        return context

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




