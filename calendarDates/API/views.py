from rest_framework.viewsets import ModelViewSet
from calendarDates.API.serializers import CalendarDatesSerializer
from calendarDates.models import calendarDate

class CalendarApiViewSet(ModelViewSet):
    serializer_class=CalendarDatesSerializer
    queryset=calendarDate.objects.all()