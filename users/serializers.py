from rest_framework import serializers
from users.models import CustomUser  

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'username', 'membership_type', 
                  'membership_start_date', 'membership_expiry_date', 'is_active', 'is_staff']
