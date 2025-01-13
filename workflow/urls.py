from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerformanceReviewViewSet

router = DefaultRouter()
router.register(r'performance-reviews', PerformanceReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]