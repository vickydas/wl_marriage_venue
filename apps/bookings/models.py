from django.db import models
from django.conf import settings
from apps.venues.models import Venue

# Create your models here.

class Booking(models.Model):

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='bookings',
        on_delete=models.CASCADE
    )

    venue = models.ForeignKey(
        Venue,
        related_name='bookings',
        on_delete=models.CASCADE
    )

    from_date = models.DateField()
    to_date = models.DateField()

    purpose = models.CharField(max_length=255, null=True, blank=True)

    payment_proof = models.FileField(
        upload_to='bookings/payment_proofs/',
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.email} - {self.venue.name} ({self.from_date} to {self.to_date})"