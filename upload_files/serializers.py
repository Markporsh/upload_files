from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate_file(value):
        valid_extensions = ['.txt', '.jpeg', '.png']
        if not any(value.name.lower().endswith(ext) for ext in valid_extensions):
            raise serializers.ValidationError(f'Только файлы типа {", ".join(valid_extensions)} поддерживаются')
        return value

    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at', 'processed')
