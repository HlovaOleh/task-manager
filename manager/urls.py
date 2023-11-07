from django.urls import path

from .views import (
    TaskListView,
    TaskDetailView,
    WorkerListView,
    WorkerDetailView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
]

app_name = "manager"
