from django.urls import path

from .views import (
    TaskListView,
    TaskDetailView,
    WorkerListView,
    WorkerDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path(
        "worker/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "worker/create/",
        WorkerCreateView.as_view(),
        name="worker-create",
    ),
    path(
        "worker/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "worker/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
]

app_name = "manager"
