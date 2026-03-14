from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from workers.models import Worker, Resume
from workers.forms import WorkerCreateForm, WorkerSearchForm


# Create your views here.
# def all_workers(request):
#     context = {
#         'all_workers': Worker.objects.all()
#     }
#
#     return render(request, 'workers/worker-all.html', context)

# CRUD: Create, Read, Update, Delete

class WorkerListView(ListView):
    model = Worker
    template_name = 'workers/worker-all.html'
    context_object_name = 'all_workers'


class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'workers/worker-detail.html'
    context_object_name = 'worker'


class WorkerDeleteView(PermissionRequiredMixin, DeleteView):
    model = Worker
    template_name = 'workers/worker-delete.html'
    context_object_name = 'worker'
    success_url = reverse_lazy('all_workers')
    permission_required = 'workers.delete_worker'  # app_label.action_model (add, change, delete, view)


class WorkerCreateView(PermissionRequiredMixin, CreateView):
    # # --------- 1
    # model = Worker
    # fields = ['name', 'salary', 'note']

    # --------- 2
    model = Worker
    form_class = WorkerCreateForm

    template_name = 'workers/worker-create.html'
    permission_required = 'workers.add_worker'

    def get_success_url(self):
        return reverse('worker_detail', kwargs={'pk': self.object.id})

# workers.change_worker

class ResumeCreateView(PermissionRequiredMixin, CreateView):
    model = Resume
    fields = ['description']
    template_name = 'workers/resume-create.html'
    permission_required = 'workers.add_resume'

    def dispatch(self, request, *args, **kwargs):
        self.worker = get_object_or_404(Worker, pk=kwargs['worker_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['worker'] = self.worker
        return context

    def form_valid(self, form):
        form.instance.worker = self.worker
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('worker_detail', kwargs={'pk': self.worker.id})


class WorkerSearchView(View):
    template_name = 'workers/worker-search.html'

    def get(self, request):
        form = WorkerSearchForm(request.GET or None)
        all_workers = Worker.objects.all()

        if form.is_valid():
            form_data = form.cleaned_data

            name = form_data.get('name')
            min_salary = form_data.get('min_salary')
            max_salary = form_data.get('max_salary')

            if name:
                all_workers = all_workers.filter(name__icontains=name)

            if min_salary:
                all_workers = all_workers.filter(salary__gte=min_salary)

            if max_salary:
                all_workers = all_workers.filter(salary__lte=max_salary)


        return render(request, self.template_name, {'form': form, 'workers': all_workers})
