from rest_framework import serializers
import api.models

class HSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Hauntedhouse
        fields = '__all__'

class RSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Renthouses
        fields = '__all__'

class FSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Firebrigade
        fields = '__all__'

class PSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Policestation
        fields = '__all__'

class CSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Cvs
        fields = '__all__'

class ESerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Excellentmarket
        fields = '__all__'

class HrtSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Hardwareretail
        fields = '__all__'

class HstSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Hardwarestore
        fields = '__all__'

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Restaurant
        fields = '__all__'

class WSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.WChild
        fields = '__all__'