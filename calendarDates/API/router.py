from rest_framework.routers import DefaultRouter
from calendarDates.API.views import CalendarApiViewSet

router_calendar=DefaultRouter()

router_calendar.register(

    prefix='Agenda', basename='Agenda', viewset=CalendarApiViewSet
)
