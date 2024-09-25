import csv
from api.models import Supermarket
from django.core.management.base import BaseCommand

def run():
    Supermarket.objects.all().delete()
    supermarkets= ['auchan','carrefour','casino']

    for supermarket in supermarkets:
        path =f'/Users/minh/Desktop/Comparator/Scrap/Data_base/drivesScraped/list_drives_{supermarket}Scraped.csv'
        with open(path, 'r', encoding='utf8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row

            for row in reader:
    
                supermarket = Supermarket.objects.create(
                    supermarket=row[1],
                    department = row[2],
                    nom_drive = row[3],
                    nom_driveUrl = row[4],
                    city = row[5],
                    adresse = row[6],
                    latitude = row[7],
                    longitude=row[8],
                    dateScraped= row[10],
                        )
        print(f'import succesful {supermarket}')
