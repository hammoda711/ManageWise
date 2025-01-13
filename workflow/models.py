from django.db import models

# Create your models here.
from django.db import models
from django_fsm import FSMField, transition

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Additional employee details can be added here

    def __str__(self):
        return self.name

class PerformanceReview(models.Model):
    PENDING_REVIEW = 'pending_review'
    REVIEW_SCHEDULED = 'review_scheduled'
    FEEDBACK_PROVIDED = 'feedback_provided'
    UNDER_APPROVAL = 'under_approval'
    REVIEW_APPROVED = 'review_approved'
    REVIEW_REJECTED = 'review_rejected'

    STAGE_CHOICES = [
        (PENDING_REVIEW, 'Pending Review'),
        (REVIEW_SCHEDULED, 'Review Scheduled'),
        (FEEDBACK_PROVIDED, 'Feedback Provided'),
        (UNDER_APPROVAL, 'Under Approval'),
        (REVIEW_APPROVED, 'Review Approved'),
        (REVIEW_REJECTED, 'Review Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_reviews')
    review_date = models.DateField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    stage = FSMField(choices=STAGE_CHOICES, default=PENDING_REVIEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.employee.name} - {self.get_stage_display()}"

    # Transitions
    @transition(field=stage, source='pending_review', target='review_scheduled')
    def schedule_review(self, date):
        self.review_date = date

    @transition(field=stage, source='review_scheduled', target='feedback_provided')
    def provide_feedback(self, feedback):
        self.feedback = feedback

    @transition(field=stage, source='feedback_provided', target='under_approval')
    def submit_for_approval(self):
        pass

    @transition(field=stage, source='under_approval', target='review_approved')
    def approve_review(self):
        pass

    @transition(field=stage, source='under_approval', target='review_rejected')
    def reject_review(self):
        pass

    @transition(field=stage, source='review_rejected', target='feedback_provided')
    def update_feedback(self, updated_feedback):
        self.feedback = updated_feedback
