from django.urls import path
from workers.views import WorkerListView, WorkerDetailView, WorkerDeleteView, WorkerCreateView, ResumeCreateView, WorkerSearchView


urlpatterns = [
    path('all/', WorkerListView.as_view(), name='all_workers'),
    path('create/', WorkerCreateView.as_view(), name='worker_create'),
    path('<int:pk>/', WorkerDetailView.as_view(), name='worker_detail'),
    path('<int:pk>/delete/', WorkerDeleteView.as_view(), name='worker_delete'),

    path('<int:worker_id>/resume/create/', ResumeCreateView.as_view(), name='resume_create'),
    path('search/', WorkerSearchView.as_view(), name='worker_search'),
]
