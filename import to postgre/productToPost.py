
from psycopg2 import sql
import psycopg2
import pandas as pd

user = 'minh'
# Connect to the PostgreSQL database
conn = psycopg2.connect(
   dbname='comparator',
   user=user,
   password='07970797',
   host='database-1.cdjhn3xzznk3.eu-north-1.rds.amazonaws.com',
   port='5432'
)
print('connect succes')

# Create a cursor object
conn.autocommit = True
cursor = conn.cursor()

#drop table product
dropTable   = '''DROP TABLE product;'''
cursor.execute(dropTable)

#create table product
sql = '''CREATE TABLE product(supermarket varchar(255),\
nom_drive varchar(255),"nom_driveUrl" varchar(255),rayon_principal varchar(255),rayon_secondaire varchar(255),\
nom_produit varchar(255),prix_produit decimal(10, 2),prix_ratio decimal(10, 2),unite varchar(50), lien_image varchar(255));'''
cursor.execute(sql)


#import all product
dfList1 = pd.read_csv('/Users/minh/Desktop/Comparator/Scrap/Data_base/drivesScraped/list_drives_auchanScraped.csv')
dfList2 = pd.read_csv('/Users/minh/Desktop/Comparator/Scrap/Data_base/drivesScraped/list_drives_carrefourScraped.csv')
dfList3 = pd.read_csv('/Users/minh/Desktop/Comparator/Scrap/Data_base/drivesScraped/list_drives_casinoScraped.csv')

frames = [dfList1, dfList2, dfList3]

dfSupermarket= pd.concat(frames)
for i,supermarket in enumerate(dfSupermarket['supermarket']):
    department = dfSupermarket.iloc[i]["department"]
    city = dfSupermarket.iloc[i]["city"]
    dateScraped= dfSupermarket.iloc[i]["date_scraped"]
    nom_drive = dfSupermarket.iloc[i]["nom_drive"]

    path = f'/Users/minh/Desktop/Comparator/Scrap/Data_base/{department}/{city}/{nom_drive}/{dateScraped}/{supermarket}_produits.csv'
    
    with open(path, 'r') as f:
        next(f)
        cursor.copy_from(f, 'product', sep=',')
    print(f'import succes {nom_drive}')

#create index
sql2= '''ALTER TABLE product \
ADD COLUMN id serial;'''
cursor.execute(sql2)

conn.commit()
conn.close()

print("CSV data imported successfully into PostgreSQL.")
