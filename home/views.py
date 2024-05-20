from rest_framework.decorators import APIView
from rest_framework.response import Response
# from rest_framework.decorators import api_view


# @api_view(['GET', 'POST', 'PUT'])
# def home(request):
# 	return Response({'name': 'seyed'})

class Home(APIView):
	def get(self, request):
		return Response({'name': 'seyed'})
