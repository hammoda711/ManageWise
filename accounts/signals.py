# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.exceptions import ObjectDoesNotExist
# from .models import CustomUser
# from company.models import Employee

# @receiver(post_save, sender=CustomUser)
# def create_employee_for_user(sender, instance, created, **kwargs):
#     """
#     Creates an Employee object when a user with 'employee' role is created.
#     """
#     if created and instance.role == 'employee':
#         try:
#             # Create the Employee object linked to the user
#             Employee.objects.create(user=instance)
#         except ObjectDoesNotExist:
#             pass  # Handle if any data is missing

# # Ensure that the signal is connected during app initialization
