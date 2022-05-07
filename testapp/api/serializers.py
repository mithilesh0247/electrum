from rest_framework.serializers import ModelSerializer
from testapp.models import Movie
class MovieSerializer(ModelSerializer):
	class Meta:
		model=Movie
		fields='__all__'