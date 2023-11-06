from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import TaskType, Task, Worker, Position


def index(request: HttpRequest) -> HttpResponse:
    task_type_count = TaskType.objects.count()
    task_count = Task.objects.count()
    workers_count = Worker.objects.count()
    position_count = Position.objects.count()
    context = {
        "task_type_count": task_type_count,
        "task_count": task_count,
        "workers_count": workers_count,
        "position_count": position_count
    }
    return render(request, "manager/index.html", context=context)
