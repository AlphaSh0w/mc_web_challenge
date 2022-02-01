from django.urls import path
from super_heroes.views import SuperHeroList,SuperHeroDetail
urlpatterns = [
    path('superheroes/', SuperHeroList.as_view(), name='superhero_list'),
    path('superheroes/<int:pk>/',SuperHeroDetail.as_view(), name='superhero_detail')
]