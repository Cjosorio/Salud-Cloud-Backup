from rest_framework import serializers
from .models import BackupWithError

class BackupWithErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackupWithError
        fields = '__all__'