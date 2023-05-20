from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
        # excluded = ['[updated_now]']

class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        exclude = ['id']
        read_only_fields = ['created_at', 'updated_at']

class ToDoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        


