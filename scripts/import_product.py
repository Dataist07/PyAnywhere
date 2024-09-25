import csv
from api.models import Supermarket, Product



# Loop through the supermarkets and import the CSV data
def run():
    Product.objects.all().delete()
    supermarkets = Supermarket.objects.all()
    
    for supermarket in supermarkets:
        sup =supermarket.supermarket
        department = supermarket.department
        city = supermarket.city
        nom_drive = supermarket.nom_drive
        dateScraped = supermarket.dateScraped 
        path =f'/Users/minh/Desktop/Comparator/Scrap/Datascrap/Data_base/{department}/{city}/{nom_drive}/{dateScraped}/{sup}_produits.csv'
        
        try : 
            
            with open(path, 'r', encoding='utf8') as f:
                print(nom_drive)
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    
                    # Create a new Product object with the data from the CSV row
                    product = Product.objects.create(
                        supermarket=row[1],
                        nom_drive=row[2],
                        nom_driveUrl=row[3],
                        shelve=row[4],
                        name=row[6],
                        price=float(row[7]),
                        price_per_quantity=float(row[8]),
                        quantity_unit=row[9],
                        url_image=row[10]
                    )
                print(f'import succesful {nom_drive}')
        except:
            pass