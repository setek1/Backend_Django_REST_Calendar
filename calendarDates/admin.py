from django.contrib import admin
from calendarDates.models import calendarDate

# Register your models here.

@admin.register(calendarDate)
class CalendarDateAdmin(admin.ModelAdmin):
    pass