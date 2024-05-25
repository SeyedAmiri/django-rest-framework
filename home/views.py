from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.decorators import api_view	# for fbv


class Home(APIView):
	permission_classes = [IsAuthenticated,]

	def get(self, request):
		persons = Person.objects.all()
		serialize_data = PersonSerializer(instance=persons, many=True)
		# persons = Person.objects.get(name='amir')
		# serialize_data = PersonSerializer(instance=persons)
		return Response(data=serialize_data.data)


# class Home(APIView):
# 	def get(self, request):
# 		name = request.query_params['name']
# 		return Response({'name': name})
#
# 	def post(self, request):
# 		data = request.data
# 		return Response(data)



# @api_view(['GET', 'POST', 'PUT'])
# def home(request):
# 	return Response({'name': 'seyed'})