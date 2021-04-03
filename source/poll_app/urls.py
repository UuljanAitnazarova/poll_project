from django.urls import path

from poll_app.views import (
                            PollListView,
                            PollChoicesView,
                            PollCreateView,
                            PollUpdateView,
                            PollDeleteView,
                            ChoiceCreateView,
                            ChoiceUpdateView,
                            ChoiceDeleteView,
)

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list'),
    path('<int:pk>/', PollChoicesView.as_view(), name='poll_detail'),
    path('create/', PollCreateView.as_view(), name='poll_create'),
    path('<int:pk>/update/', PollUpdateView.as_view(), name='poll_update'),
    path('<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
    path('<int:pk>/choices/create/', ChoiceCreateView.as_view(), name='choice_create'),
    path('choices/<int:pk>/update', ChoiceUpdateView.as_view(), name='choice_update'),
    path('choices/<int:pk>/delete', ChoiceDeleteView.as_view(), name='choice_delete'),
]