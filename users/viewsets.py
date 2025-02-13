from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]  # Restricts access to authenticated users

    def get_queryset(self):
        # Filter the queryset to only return the authenticated user
        return CustomUser.objects.filter(phone_number=self.request.user.phone_number)
