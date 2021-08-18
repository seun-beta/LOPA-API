from django.urls import path

from . import views

app_name = "lopa"

urlpatterns = [
    path('cause/<int:cause_id>', views.CauseData.as_view()),
    path('cause_barrier/<int:cause_barrier_id>', views.CauseBarrierData.as_view()),
    path('consequence/<int:consequence_id>', views.ConsequenceData.as_view()),
    path('consequence_barrier/<int:pk>', views.ConsequenceBarrierData.as_view()),
    path('event/<int:event_id>', views.EventData.as_view()),
]