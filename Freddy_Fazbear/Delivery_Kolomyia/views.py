from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import viewsets
from .models import Dish,Customer
from .serializers import MyModelSerializer,CustomerSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = MyModelSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

@api_view(['POST'])
def Auth(request):
    # Отримайте дані з запиту
    data = request.data
    dbInfo=Customer.getAuthInfo()
    
    for item in dbInfo:
            if data.get('field_to_compare') == item.field_to_compare:
                return Response({'message': 'success'})
    return Response({'message': 'fail'})

# Create your views here.
