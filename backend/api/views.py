from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        
        #data = model_to_dict(model_data)
        data = ProductSerializer(instance).data
    return Response(data)