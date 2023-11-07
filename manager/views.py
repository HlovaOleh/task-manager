from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Worker


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.all()
    paginate_by = 5


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    queryset = Worker.objects.select_related("position")
    paginate_by = 5


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("manager:worker-list")
    template_name = "manager/worker_form.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = "__all__"
    success_url = reverse_lazy("manager:worker-list")
    template_name = "manager/worker_form.html"


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:worker-list")
    template_name = "manager/worker_confirm_delete.html"


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = Task.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["task_list"] = self.object.assignees.select_related("tasks")
        return context


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_confirm_delete.html"
