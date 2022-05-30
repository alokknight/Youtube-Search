from rest_framework import serializers

class WhiskySerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    alchohol_content =serializers.IntegerField(max_value=None, min_value=None)
    malic_acid       =serializers.IntegerField(max_value=None, min_value=None)
    Ash              =serializers.IntegerField(max_value=None, min_value=None)
    alc_ash          =serializers.IntegerField(max_value=None, min_value=None)
    Magnesium        =serializers.IntegerField(max_value=None, min_value=None)
    Phenols          =serializers.IntegerField(max_value=None, min_value=None)
    Flavanoid        =serializers.IntegerField(max_value=None, min_value=None)
    NFPhelons        =serializers.IntegerField(max_value=None, min_value=None)
    Cyacnins         =serializers.IntegerField(max_value=None, min_value=None)
    Intensity        =serializers.IntegerField(max_value=None, min_value=None)
    Hue              =serializers.IntegerField(max_value=None, min_value=None)
    OD280            =serializers.IntegerField(max_value=None, min_value=None)
    Proline          =serializers.IntegerField(max_value=None, min_value=None)
    def create(self,validated_data):
        return WhiskySerializer.create(**validated_data)


































