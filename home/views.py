from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Person, Question, Answer
from .serializers import PersonSerializer,QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view	# for fbv
from rest_framework import status
from permissions import IsOwnerOrReadOnly


class Home(APIView):
	permission_classes = [IsAuthenticated,]

	def get(self, request):
		persons = Person.objects.all()
		serialize_data = PersonSerializer(instance=persons, many=True)
		# persons = Person.objects.get(name='amir')
		# serialize_data = PersonSerializer(instance=persons)
		return Response(data=serialize_data.data)


class QuestionListView(APIView):
	def get(self, request):
		questions = Question.objects.all()
		srz_data = QuestionSerializer(instance=questions, many=True).data
		return Response(srz_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
	permission_classes = [IsAuthenticated,]
	def post(self, request):
		srz_data = QuestionSerializer(data=request.data)
		if srz_data.is_valid():
			srz_data.save()
			return Response(srz_data.data, status=status.HTTP_201_CREATED)
		return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
	permission_classes = [IsOwnerOrReadOnly,]

	def put(self, request, pk):
		question = Question.objects.get(pk=pk)
		self.check_object_permissions(request, question)
		srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
		if srz_data.is_valid():
			srz_data.save()
			return Response(srz_data.data, status=status.HTTP_200_OK)
		return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
	permission_classes = [IsOwnerOrReadOnly,]

	def delete(self, request, pk):
		question = Question.objects.get(pk=pk)
		self.check_object_permissions(request, question)
		question.delete()














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