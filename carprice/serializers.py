from rest_framework import serializers
Fuel_Type=(
    ('Petrol','Petrol'),
    ('Diesel','Diesel'),
    ('CNG','CNG'),
)
Seller_Type=(
    ('Dealer','Dealer'),
    ('Individual','Individual'),
)
Transmission_Mannual=(
    ('Manual_Car','Manual_Car'),
    ('Automatic_Car','Automatic_Car'),
)
class CarpriceSerializer(serializers.Serializer):
    """Your data serializer, define your fields here."""
    Year                  =serializers.IntegerField(max_value=None,  min_value=None)
    Present_Price         =serializers.IntegerField(max_value=None,  min_value=None)
    Kms_Driven            =serializers.IntegerField(max_value=None,  min_value=None)
    Owner                 =serializers.IntegerField(max_value=None,  min_value=None)
    Fuel_Type_Petrol      =serializers.ChoiceField (choices=Fuel_Type )
    Seller_Type_Individual=serializers.ChoiceField (choices=Seller_Type )
    Transmission_Mannual  =serializers.ChoiceField (choices=Transmission_Mannual)
    def create(self,validated_data):
        return CarpriceSerializer.create(**validated_data)
