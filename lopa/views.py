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

    def get(self, request, event_id):
        try:
            cause = Cause.objects.filter(event_id=event_id)
            cause_serializer = CauseSerializer(cause, many=True)
            return Response(cause_serializer.data, status=200)
        except Cause.DoesNotExist:
            return Response(None, status=400)


class CauseBarrierData(APIView):
    
    def get(self, request, cause_id):
        try:
            cause_barrier = CauseBarrier.objects.filter(cause_id=cause_id)
            cause_barrier_serializer = CauseBarrierSerializer(cause_barrier, many=True)
            return Response(cause_barrier_serializer.data, status=200)
        except CauseBarrier.DoesNotExist:
            return Response(None, status=400)

class ConsequenceData(APIView):
    
    def get(self, request, event_id):
        try:
            consequence = Consequence.objects.filter(event_id=event_id)
            consequence_serializer = ConsequenceSerializer(consequence, many=True)
            return Response(consequence_serializer.data, status=200)
        except Consequence.DoesNotExist:
            return Response(None, status=400)



class ConsequenceBarrierData(APIView):
    
    def get(self, request, consequence_id):
        try:
            consequence_barrier = ConsequenceBarrier.objects.filter(consequence_id=consequence_id)
            consequence_barrier_serializer = ConsequenceBarrierSerializer(consequence_barrier, many=True)
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
