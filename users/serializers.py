from rest_framework import serializers
from users.models import CustomUser  # Import your CustomUser model

class CustomUserSerializer(serializers.ModelSerializer):
    # You can add any additional fields or methods you want here
    # For example, you may want to display the membership type as a string

    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'username', 'membership_type', 
                  'membership_start_date', 'membership_expiry_date', 'is_active', 'is_staff']
