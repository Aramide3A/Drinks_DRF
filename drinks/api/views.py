from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class drinkview(APIView):
    def get(self, request):
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = DrinkSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class UpdateDrinkView(APIView):
    def get(self,  request, id):
        drinks = Drink.objects.get(pk=id)
        serializer = DrinkSerializer(drinks)
        return Response(serializer.data)
    def put(self, request, id):
        drinks = Drink.objects.get(pk = id)
        serializer = DrinkSerializer(instance=drinks, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self, request, id):
        drink = Drink.objects.get(pk = id)
        drink.delete()
        return Response({'deleted successfully'}) 