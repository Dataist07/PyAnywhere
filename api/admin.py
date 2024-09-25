from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Supermarket, AuchanProduct,CarrefourProduct,CasinoProduct,LeclercProduct,IntermarcheProduct,CarrefourMarketProduct,HyperUProduct,SuperUProduct])