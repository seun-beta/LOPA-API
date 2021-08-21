from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Cause, CauseBarrier, Consequence, ConsequenceBarrier, Event

from .serializers import CauseSerializer, CauseBarrierSerializer, \
    EventSerializer, ConsequenceSerializer, ConsequenceBarrierSerializer 
from lopa import serializers

class EventList(APIView):

    def get(self, request):
        events = Event.objects.all()
        event_datas = EventSerializer(events, many=True)
        return Response(event_datas.data)


class CauseData(APIView):

    def get(self, request, cause_id):
        try:
            cause = Cause.objects.get(pk=cause_id)
            cause_serializer = CauseSerializer(cause)
            return Response(cause_serializer.data, status=200)
        except Cause.DoesNotExist:
            return Response(None, status=400)


class CauseBarrierData(APIView):
    
    def get(self, request, cause_barrier_id):
        try:
            cause_barrier = CauseBarrier.objects.get(pk=cause_barrier_id)
            cause_barrier_serializer = CauseBarrierSerializer(cause_barrier)
            return Response(cause_barrier_serializer.data, status=200)
        except CauseBarrier.DoesNotExist:
            return Response(None, status=400)

class ConsequenceData(APIView):
    
    def get(self, request, consequence_id):
        try:
            consequence = Consequence.objects.get(pk=consequence_id)
            consequence_serializer = ConsequenceSerializer(consequence)
            return Response(consequence_serializer.data, status=200)
        except Consequence.DoesNotExist:
            return Response(None, status=400)



class ConsequenceBarrierData(APIView):
    
    def get(self, request, consequence_barrier_id):
        try:
            consequence_barrier = ConsequenceBarrier.objects.get(pk=consequence_barrier_id)
            consequence_barrier_serializer = ConsequenceBarrierSerializer(consequence_barrier)
            return Response(consequence_barrier_serializer.data, status=200)
        except ConsequenceBarrier.DoesNotExist:
            return Response(None, status=400)


class EventData(APIView):
    
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
            event_serializer = EventSerializer(event)
            return Response(event_serializer.data, status=200)
        except Event.DoesNotExist:
            return Response(None, status=400)
