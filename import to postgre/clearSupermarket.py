import pandas as pd

supermarkets= ['auchan','carrefour','casino']
for supermarket in supermarkets:
    path =f'/Users/minh/Desktop/Comparator/Scrap/Data_base/drivesScraped/list_drives_{supermarket}Scraped.csv'
    df = pd.read_csv(path)
    listSupermarket =[]
    for i,nom in enumerate(df['id']):
        #ajout dans les drives scraped
        dict_drive ={
                "supermarket": df.iloc[i]['supermarket'].replace(",",""),
                "department": str(df.iloc[i]['department']).replace(",",""),
                "nom_drive": df.iloc[i]['nom_drive'].replace(",",""),
                "nom_driveUrl" : df.iloc[i]['nom_driveUrl'].replace(",",""),
                'city': df.iloc[i]['city'].replace(",",""),
                "adresse": df.iloc[i]['adresse'].replace(",",""),
                "latitude": df.iloc[i]['latitude'],
                "longitude": df.iloc[i]['longitude'],          
                "lien_drive" : df.iloc[i]['lien_drive'].replace(",",""),
                "date_scraped": df.iloc[i]['date_scraped'].replace(",","")
            }
        listSupermarket.append(dict_drive)
    df_produits = pd.DataFrame(listSupermarket)
    df_produits.to_csv(path, index=False)
    print(f'nettoye complet {supermarket}')