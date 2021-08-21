from django.urls import path

from . import views

app_name = "lopa"

urlpatterns = [
    path("",views.EventList.as_view()),
    path('cause/<cause_id>', views.CauseData.as_view()),
    path('cause_barrier/<cause_barrier_id>', views.CauseBarrierData.as_view()),
    path('consequence/<consequence_id>', views.ConsequenceData.as_view()),
    path('consequence_barrier/<consequence_barrier_id>', views.ConsequenceBarrierData.as_view()),
    path('event/<event_id>', views.EventData.as_view()),
]