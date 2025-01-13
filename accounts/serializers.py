from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Import the User model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('employee', 'Employee')], default='employee')

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'role']
    
    def create(self, validated_data):
        role = validated_data.pop('role', 'employee')  # Get the role from validated data, default to 'employee'
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            role=role,  # Pass the role value here
        )
        return user

