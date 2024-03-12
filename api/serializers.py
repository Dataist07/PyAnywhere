from rest_framework import serializers
from .models import *

class AuchanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuchanProduct
        fields = ('__all__')

class CarrefourProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrefourProduct
        fields = ('__all__')

class LeclercProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeclercProduct
        fields = ('__all__')

class CasinoProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasinoProduct
        fields = ('__all__')

class IntermarcheProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntermarcheProduct
        fields = ('__all__')

class SupermarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarket
        fields = ('__all__')
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')