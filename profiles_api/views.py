# from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
     """Test API View"""

     # self siempre es requerido
     def get(self, request, format=None):
          """Returns a list of APIView features"""
          an_apiview = [
               'Uses HTTP Methods as function(get, post, patch, put, delete)',
               'Is similar to a traditional Django View',
               'Gives you the most control over you application logic',
               'Is mapped manually to URLs',
          ]

          return Response({'message': 'Hello!', 'an_apiview': an_apiview})