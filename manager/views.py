from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import TaskType, Task, Worker, Position


# def index(request: HttpRequest) -> HttpResponse:
#     context = {
#         "task_type_count": TaskType.objects.count(),
#         "task_count": Task.objects.count(),
#         "workers_count": Worker.objects.count(),
#         "position_count": Position.objects.count()
#     }
#     return render(request, "manager/index.html", context=context)


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    paginate_by = 5


class WorkerListView(generic.ListView):
    model = Worker
    queryset = Worker.objects.select_related("position")
    paginate_by = 5


class WorkerDetailView(generic.DetailView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task
    queryset = Task.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["task_list"] = self.object.assignees.select_related("tasks")
        return context
