from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerializer,QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.decorators import api_view	# for fbv
from rest_framework import status



class Home(APIView):
	permission_classes = [IsAuthenticated,]

	def get(self, request):
		persons = Person.objects.all()
		serialize_data = PersonSerializer(instance=persons, many=True)
		# persons = Person.objects.get(name='amir')
		# serialize_data = PersonSerializer(instance=persons)
		return Response(data=serialize_data.data)




class QuestionView(APIView):
	def get(self, request):
		questions = Question.objects.all()
		srz_data = QuestionSerializer(instance=questions, many=True).data
		return Response(srz_data, status=status.HTTP_200_OK)

	def post(self, request):
		pass

	def put(self, request, pk):
		pass

	def delete(self, request, pk):
		pass

















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