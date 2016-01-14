from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def hello(request):
    return Response({'message':'Hello, World!'})

@api_view(['GET'])
def hello2(request, id):
    w = 'Hello %s' % id
    return Response({'message':w})

@api_view(['GET','POST'])
def hello3(request):
    if request.method == 'POST':
        return Response({'message': "Got some data", 'data':request.data})
    return Response({'message':'Hello, World!'})

