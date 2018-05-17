from rest_framework import serializers
from Database.models import Question, Objective, Team, Event

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_id','content')

class TeamSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Team
        fields=('owner','name')

class ObjectiveSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Objective
        fields = ('name','code','description','questions')

class EventSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)
    objectives = ObjectiveSerializer(many=True)

    class Meta:
        model = Event
        fields = ('name','startTime','endTime','teams','objectives')

