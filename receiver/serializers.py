from receiver.models import Record
from rest_framework import serializers

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['created', 'owner', 'temperature', 'message']
