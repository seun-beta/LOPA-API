from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Cause, CauseBarrier, Consequence, ConsequenceBarrier, Event

from .serializers import CauseSerializer, CauseBarrierSerializer, \
    EventSerializer, ConsequenceSerializer, ConsequenceBarrierSerializer 
from lopa import serializers


class IndexView(View):
    def get(self, request):
        event_list = Event.objects.all()
        ctx = {'event_list': event_list}
        return render(request, 'lopa/index.html', ctx)


class DataView(View):

    def get(self, request):
        pass


class CauseData(APIView):

    def get(self, request, cause_id):
        cause = Cause.objects.all().values("cause_id", "description", "initial_frequency", "event_id", "target_frequency")
        cause_list = list(cause)
        data = cause_list 
        new_data = CauseSerializer(data, many=True)
        return Response(new_data.data)

class CauseBarrierData(APIView):
    
    def get(self, request, cause_barrier_id):
        cause_barrier = CauseBarrier.objects.all().values("cause_barrier_id", "description", "pfd", "cause_id")
        cause_barrier_list = list(cause_barrier)
        data = cause_barrier_list 
        new_data = CauseBarrierSerializer(data, many=True)
        return Response(new_data.data)


class ConsequenceData(APIView):
    
    def get(self, request, consequence_id):
        consequence = Consequence.objects.all().values("consequence_id", "description", "initial_frequency", "target_frequency")
        consequence_list = list(consequence)
        data = consequence_list 
        new_data = ConsequenceSerializer(data, many=True)
        return Response(new_data.data)


class ConsequenceBarrierData(APIView):
    
    def get(self, request, consequence_barrier_id):
        consequence_barrier = ConsequenceBarrier.objects.get(pk=consequence_barrier_id)
        new_data = ConsequenceBarrierSerializer(consequence_barrier, many=True)
        return Response(new_data.data)

class EventData(APIView):
    
    def get(self, request, event_id):
        event = Event.objects.all().values("event_id","description", "cause_id", "consequence_id")
        event_list = list(event)
        data = event_list 
        new_data = EventSerializer(data, many=True)
        return Response(new_data.data)
