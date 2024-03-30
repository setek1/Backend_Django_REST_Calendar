from rest_framework.serializers import ModelSerializer

from calendarDates.models import calendarDate

class CalendarDatesSerializer(ModelSerializer):
    class Meta:
        model=calendarDate
        fields='__all__'