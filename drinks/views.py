from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        #get all the drinks
        drinks = Drink.objects.all()
        #serialize them
        serializer = DrinkSerializer(drinks, many=True)
        #return json
        return JsonResponse({'drinks': serializer.data})
    
    if request.method == 'POST':
        #get data from the request
        serializer = DrinkSerializer(data=request.data)
        #check if that data is valid or not
        if serializer.is_valid():
            #save it
            serializer.save()
            #return response of that data as JSON specific
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    try:
        #get drink object by id
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #get data of that drink object
        serializer = DrinkSerializer(drink)
        #return response of that data
        #this response is NOT JSON specific
        return Response(serializer.data)
    elif request.method == 'PUT':
        #get data of that drink object and the request
        serializer = DrinkSerializer(drink, data=request.data)
        #check if that data is valid or not
        if serializer.is_valid():
            #save it
            serializer.save()
            #return response of that data
            return Response(serializer.data)
        # return status of an error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)