from ninja import ModelSchema
from api.models import Supermarket, AuchanProduct,CarrefourProduct,CasinoProduct,LeclercProduct,IntermarcheProduct

class SupermarketSchema(ModelSchema):
    class Meta:
        model = Supermarket
        fields = ('id','supermarket', 'department','nom_drive','nom_driveUrl','city','adresse','latitude','longitude','lien_drive','dateScraped')

class AuchanProductSchema(ModelSchema):
    class Meta:
        model = AuchanProduct
        fields = ('id','supermarket', 'nom_driveUrl','rayon_principal','nom_produit','prix_produit','prix_ratio','unite','lien_image')

class CarrefourProductSchema(ModelSchema):
    class Meta:
        model = CarrefourProduct
        fields = ('id','supermarket', 'nom_driveUrl','rayon_principal','nom_produit','prix_produit','prix_ratio','unite','lien_image')

class CasinoProductSchema(ModelSchema):
    class Meta:
        model = CasinoProduct
        fields = ('id','supermarket', 'nom_driveUrl','rayon_principal','nom_produit','prix_produit','prix_ratio','unite','lien_image')

class LeclercProductSchema(ModelSchema):
    class Meta:
        model = LeclercProduct
        fields = ('id','supermarket', 'nom_driveUrl','rayon_principal','nom_produit','prix_produit','prix_ratio','unite','lien_image')

class IntermarcheProductSchema(ModelSchema):
    class Meta:
        model = IntermarcheProduct
        fields = ('id','supermarket', 'nom_driveUrl','rayon_principal','nom_produit','prix_produit','prix_ratio','unite','lien_image')
