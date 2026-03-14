from PIL.TiffImagePlugin import SAVE_INFO
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS

from workers.models import Worker, Resume
from workers_api.serializers import WorkerSerializer, ResumeSerializer


# Низький рівень: APIView, вручну прописуємо методи (get, post)
# Високий рівень: ViewSet, адаптований під CRUD, та роботу з моделями


class IsHRPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.groups.filter(name='HR').exists()


class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsHRPermission]


class ResumeViewSet(ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsHRPermission]
