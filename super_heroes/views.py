from rest_framework import generics
from super_heroes.models import SuperHero
from super_heroes.serializers import SuperHeroSerializer

# Create your views here.

class SuperHeroList(generics.ListCreateAPIView):
    queryset = SuperHero.objects.all()
    serializer_class = SuperHeroSerializer

class SuperHeroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuperHero.objects.all()
    serializer_class = SuperHeroSerializer