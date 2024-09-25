import pandas as pd

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
    
    #nettoye df
    df_produits = pd.read_csv(path)
    list_produits =[]
    for i,nom in enumerate(df_produits['nom_produit']):
        dict_produit={
                            'supermarket'   : df_produits.iloc[i]['supermarket'].replace(",",""),
                            'nom_drive' : df_produits.iloc[i]['nom_drive'].replace(",",""),
                            'nom_driveUrl' : df_produits.iloc[i]['nom_driveUrl'].replace(",",""),
                            'rayon_principal' : df_produits.iloc[i]['rayon_principal'].replace(",",""),
                            'rayon_secondaire' : df_produits.iloc[i]['rayon_secondaire'].replace(",",""),
                            'nom_produit': str(df_produits.iloc[i]['nom_produit']).replace(",",""),
                            'prix_produit': df_produits.iloc[i]['prix_produit'],
                            'prix_ratio' : df_produits.iloc[i]['prix_ratio'],
                            'unite' : df_produits.iloc[i]['unite'].replace(",",""),
                            'lien_image': str(df_produits.iloc[i]['lien_image']).replace(",","")

                        }
        list_produits.append(dict_produit)
    df_produits = pd.DataFrame(list_produits)
    df_produits.to_csv(path, index=False)
    print(f'nettoye complet {nom_drive}')