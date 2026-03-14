from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from workers_api.views import WorkerViewSet, ResumeViewSet


router = DefaultRouter()
router.register('workers', WorkerViewSet)
router.register('resume', ResumeViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
