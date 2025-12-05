from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db import models
from .models import Event, RSVP, Review
from .serializers import EventSerializer, RSVPSerializer, ReviewSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['post'])
    def rsvp(self, request, pk=None):
        event = self.get_object()
        serializer = RSVPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=event, user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['patch'], url_path='rsvp/(?P<user_id>[^/.]+)')
    def rsvp_update(self, request, pk=None, user_id=None):
        try:
            rsvp = RSVP.objects.get(event_id=pk, user_id=user_id)
        except RSVP.DoesNotExist:
            return Response({"error": "RSVP not found"}, status=404)
        serializer = RSVPSerializer(rsvp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['post'])
    def reviews(self, request, pk=None):
        event = self.get_object()
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=event, user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get'])
    def reviews_list(self, request, pk=None):
        event = self.get_object()
        reviews = event.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
