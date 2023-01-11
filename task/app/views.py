from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import proserializer
from rest_framework import status
from .models import Product
from django.http import JsonResponse
from .tasks import data_from_csv_to_model
from django.http import HttpResponse


# Create your views here.
@api_view(['GET'])
def listpro(request):
        products = Product.objects.all()
        if request.method == 'GET':
            serializer = proserializer(products,many = True)
            return JsonResponse({"products" : serializer.data})

@api_view(['POST'])
def insert(request):
    if request.method == 'POST':
        serializer = proserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET'])
def csvins(request):
    #tasks
    arg = "/Users/florinamary/Documents/CrowdANALYTIX/celeryexp/djangocelery/task/app/data.csv"
    data_from_csv_to_model.delay(arg)
    return HttpResponse("Inserting Data from CSV to Model....")