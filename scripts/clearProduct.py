from api.models import Supermarket, Product



# Loop through the supermarkets and import the CSV data
def run():
    Product.objects.all().delete()
    Supermarket.objects.all().delete()