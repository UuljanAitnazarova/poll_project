from django.urls import path

from poll_app.views import (
                            PollListView,
                            PollDetailView,
                            PollCreateView,
                            PollUpdateView,
                            PollDeleteView,
)

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list'),
    path('<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    path('create/', PollCreateView.as_view(), name='poll_create'),
    path('<int:pk>/update/', PollUpdateView.as_view(), name='poll_update'),
    path('<int:pk>/delete/', PollDeleteView.as_view(), name='poll_delete'),
]