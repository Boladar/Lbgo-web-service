from rest_framework import serializers
from django.contrib.auth.models import User
from Database.models import Question, Objective, Team, Event

class TeamSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Team
        fields=('owner','name')

class ObjectiveSerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)
    class Meta:
        model = Objective
        fields = ('name','code','description','questions')

class EventSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)
    objectives = ObjectiveSerializer(many=True)

    class Meta:
        model = Event
        fields = ('name','startTime','teams','objectives')

