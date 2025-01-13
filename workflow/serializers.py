from rest_framework import serializers
from .models import PerformanceReview

class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = ['id', 'employee', 'review_date', 'feedback', 'stage', 'created_at', 'updated_at']
        read_only_fields = ['stage', 'created_at', 'updated_at']
