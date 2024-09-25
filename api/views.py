from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

#django filters



@api_view(['GET'])
def supermarket_list(request):
    supermarket = Supermarket.objects.all()
    serializer = SupermarketSerializer(supermarket, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_supermarket_list(request,supermarket,nom_drive):
    nom_produit = request.GET.get('nom_produit')
    if supermarket =="Auchan" :
        product = AuchanProduct.objects.filter(nom_driveUrl=nom_drive)
        if nom_produit :
            product = product.filter(nom_produit__icontains=nom_produit)
        serializer = AuchanProductSerializer(product, many=True)

    elif supermarket == "Carrefour" :
        product = CarrefourProduct.objects.filter(nom_driveUrl=nom_drive)
        if nom_produit :
            product = product.filter(nom_produit__icontains=nom_produit)
        serializer = CarrefourProductSerializer(product, many=True)
    elif supermarket == "Leclerc" :
        product = LeclercProduct.objects.filter(nom_driveUrl=nom_drive)
        if nom_produit :
            product = product.filter(nom_produit__icontains=nom_produit)
        serializer = LeclercProductSerializer(product, many=True)
    elif supermarket == "Intermarche" :
        product = IntermarcheProduct.objects.filter(nom_driveUrl=nom_drive)
        if nom_produit :
            product = product.filter(nom_produit__icontains=nom_produit)
        serializer = IntermarcheProductSerializer(product, many=True)
    elif supermarket == "Casino" :
        product = CasinoProduct.objects.filter(nom_driveUrl=nom_drive)
        if nom_produit :
            product = product.filter(nom_produit__icontains=nom_produit)
        serializer = CasinoProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_list(request,nom_drive):
    product = Product.objects.filter(nom_driveUrl=nom_drive)
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

