from rest_framework import serializers
from .models import Board, ToDoList


class BoardCreateAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TodoListAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'


class BoardListAPIViewSerializer(serializers.Serializer):
    name = serializers.CharField()
    count = serializers.IntegerField()