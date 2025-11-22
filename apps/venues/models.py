from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()

    capacity = models.IntegerField(default=0)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    
    image = models.ImageField(upload_to='venues/images/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Utility(models.Model):
    venue = models.ForeignKey(Venue, related_name='utilities', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.venue.name}"