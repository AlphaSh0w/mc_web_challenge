from rest_framework import serializers
from super_heroes.models import SuperHero

class SuperHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperHero
        fields = '__all__'
