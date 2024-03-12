from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *


@api_view(['GET'])
def supermarket_list(request):
    supermarket = Supermarket.objects.all()
    serializer = SupermarketSerializer(supermarket, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_supermarket_list(request,supermarket,nom_drive):
    if supermarket =="Auchan" :
        product = AuchanProduct.objects.filter(nom_driveUrl=nom_drive)
        serializer = AuchanProductSerializer(product, many=True)
    elif supermarket == "Carrefour" :
        product = CarrefourProduct.objects.filter(nom_driveUrl=nom_drive)
        serializer = CarrefourProductSerializer(product, many=True)
    elif supermarket == "Leclerc" :
        product = LeclercProduct.objects.filter(nom_driveUrl=nom_drive)
        serializer = LeclercProductSerializer(product, many=True)
    elif supermarket == "Intermarche" :
        product = IntermarcheProduct.objects.filter(nom_driveUrl=nom_drive)
        serializer = IntermarcheProductSerializer(product, many=True)
    elif supermarket == "Casino" :
        product = CasinoProduct.objects.filter(nom_driveUrl=nom_drive)
        serializer = CasinoProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_supermarket_list(request,nom_drive):
    product = Product.objects.filter(nom_driveUrl=nom_drive)
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

