from rest_framework import serializers

class SemanticSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    semantictext =serializers.CharField(max_length=None, min_length=None)
    def create(self,validated_data):
        return SemanticSerializer.create(**validated_data)


































