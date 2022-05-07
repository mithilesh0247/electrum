from rest_framework import viewsets
from testapp.models import Movie
from testapp.api.serializers import MovieSerializer
class MovieCRUDCBV(viewsets.ModelViewSet):
	serializer_class=MovieSerializer
	queryset=Movie.objects.all()	