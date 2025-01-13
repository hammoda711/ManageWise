from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PerformanceReview
from .serializers import PerformanceReviewSerializer
from accounts.permissions import IsAdminOrManager
from rest_framework.permissions import IsAuthenticated
class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAuthenticated,IsAdminOrManager] 

    @action(detail=True, methods=['post'])
    def schedule_review(self, request, pk=None):
        review = self.get_object()
        date = request.data.get('review_date')
        if not date:
            return Response({'error': 'Review date is required'}, status=status.HTTP_400_BAD_REQUEST)
        review.schedule_review(date=date)
        review.save()
        return Response({'status': 'Review scheduled successfully'})

    @action(detail=True, methods=['post'])
    def provide_feedback(self, request, pk=None):
        review = self.get_object()
        feedback = request.data.get('feedback')
        if not feedback:
            return Response({'error': 'Feedback is required'}, status=status.HTTP_400_BAD_REQUEST)
        review.provide_feedback(feedback=feedback)
        review.save()
        return Response({'status': 'Feedback provided successfully'})

    @action(detail=True, methods=['post'])
    def submit_for_approval(self, request, pk=None):
        review = self.get_object()
        review.submit_for_approval()
        review.save()
        return Response({'status': 'Review submitted for approval'})

    @action(detail=True, methods=['post'])
    def approve_review(self, request, pk=None):
        review = self.get_object()
        review.approve_review()
        review.save()
        return Response({'status': 'Review approved successfully'})

    @action(detail=True, methods=['post'])
    def reject_review(self, request, pk=None):
        review = self.get_object()
        review.reject_review()
        review.save()
        return Response({'status': 'Review rejected successfully'})

    @action(detail=True, methods=['post'])
    def update_feedback(self, request, pk=None):
        review = self.get_object()
        updated_feedback = request.data.get('updated_feedback')
        if not updated_feedback:
            return Response({'error': 'Updated feedback is required'}, status=status.HTTP_400_BAD_REQUEST)
        review.update_feedback(updated_feedback=updated_feedback)
        review.save()
        return Response({'status': 'Feedback updated successfully'})
