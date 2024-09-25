from ninja import NinjaAPI
from api.models import Supermarket, AuchanProduct,CarrefourProduct,CasinoProduct,LeclercProduct,IntermarcheProduct,CarrefourMarketProduct,HyperUProduct,SuperUProduct
from api.schemas import SupermarketSchema, CarrefourProductSchema


app = NinjaAPI()

@app.get("supermarkets/", response=list[SupermarketSchema])
def get_supermarkets(request):
    return Supermarket.objects.all()

@app.get("products/{supermarket}/{nom_drive}", response=list[CarrefourProductSchema])
def get_product(request,supermarket:str,nom_drive:str):
    if supermarket =="Auchan" :
        product = AuchanProduct.objects.filter(nom_driveUrl=nom_drive)
    elif supermarket == "CarrefourMarket" :
        product = CarrefourMarketProduct.objects.filter(nom_driveUrl=nom_drive)
    elif supermarket == "Carrefour" :
        product = CarrefourProduct.objects.filter(nom_driveUrl=nom_drive)
    elif supermarket == "Leclerc" :
        product = LeclercProduct.objects.filter(nom_driveUrl=nom_drive)
    elif supermarket == "Intermarche" :
        product = IntermarcheProduct.objects.filter(nom_driveUrl=nom_drive)
    elif supermarket == "Casino" :
        product = CasinoProduct.objects.filter(nom_driveUrl=nom_drive)
    elif supermarket == "HyperU" :
        product = HyperUProduct.objects.filter(nom_driveUrl=nom_drive)
    elif supermarket == "SuperU" :
        product = SuperUProduct.objects.filter(nom_driveUrl=nom_drive)
    return product

@app.get("products/{supermarket}/{nom_drive}/{nom_produit}", response=list[CarrefourProductSchema])
def get_product(request,supermarket:str,nom_drive:str,nom_produit:str):
    if supermarket =="Auchan" :
        product = AuchanProduct.objects.filter(nom_driveUrl=nom_drive)
        product = product.filter(nom_produit__icontains=nom_produit)
    elif supermarket == "Carrefour" :
        product = CarrefourProduct.objects.filter(nom_driveUrl=nom_drive)
        product = product.filter(nom_produit__icontains=nom_produit)
    elif supermarket == "Leclerc" :
        product = LeclercProduct.objects.filter(nom_driveUrl=nom_drive)
        product = product.filter(nom_produit__icontains=nom_produit)
    elif supermarket == "Intermarche" :
        product = IntermarcheProduct.objects.filter(nom_driveUrl=nom_drive)
        product = product.filter(nom_produit__icontains=nom_produit)
    elif supermarket == "Casino" :
        product = CasinoProduct.objects.filter(nom_driveUrl=nom_drive)
        product = product.filter(nom_produit__icontains=nom_produit)
    return product
