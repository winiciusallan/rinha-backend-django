from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def pessoas(request):
    return Response({"message": "oi"})

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello, world! The application is working"})

