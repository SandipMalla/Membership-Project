from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import timedelta, date

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field is required')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)

MEMBERSHIP_CHOICES = [
    ('Silver', 'Silver'),
    ('Gold', 'Gold'),
    ('Diamond', 'Diamond'),
]

MEMBERSHIP_DURATIONS = {
    'Silver': 30,
    'Gold': 90,
    'Diamond': 180,
}

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default='Silver')
    membership_start_date = models.DateField(null=True, blank=True)
    membership_expiry_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if self.membership_type and not self.membership_start_date:
            self.membership_start_date = date.today()
            self.membership_expiry_date = date.today() + timedelta(days=MEMBERSHIP_DURATIONS[self.membership_type])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number
