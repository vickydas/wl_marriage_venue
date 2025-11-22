from django.contrib import admin
from .models import Venue, Utility

# Register your models here.
class UtilityInline(admin.TabularInline):
    model = Utility
    extra = 1

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "capacity", "price_per_day")
    inlines = [UtilityInline]

    admin.site.register(Utility)