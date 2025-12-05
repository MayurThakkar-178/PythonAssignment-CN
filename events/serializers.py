from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event, RSVP, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)
    invited_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'organizer', 'location',
            'start_time', 'end_time', 'is_public', 'invited_users',
            'created_at', 'updated_at',
        ]

    def validate(self, attrs):
        start = attrs.get('start_time') or getattr(self.instance, 'start_time', None)
        end = attrs.get('end_time') or getattr(self.instance, 'end_time', None)
        if start and end and end <= start:
            raise serializers.ValidationError("end_time must be after start_time")
        return attrs

    def create(self, validated_data):
        invited = validated_data.pop('invited_users', [])
        event = Event.objects.create(**validated_data)
        if invited:
            event.invited_users.set(invited)
        return event

    def update(self, instance, validated_data):
        invited = validated_data.pop('invited_users', None)
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        if invited is not None:
            instance.invited_users.set(invited)
        return instance


class RSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSVP
        fields = ['id', 'event', 'user', 'status']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'event', 'user', 'rating', 'comment']
