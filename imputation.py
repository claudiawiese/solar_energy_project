import pandas as pd
import numpy as np


def impute_july_with_next_year(df, target_year):
   
    july_data = df[(df['Datetime'].dt.year == target_year) & (df['Datetime'].dt.month == 7)]
    
    july_data_after = df[(df['Datetime'].dt.year == target_year + 1) & (df['Datetime'].dt.month == 7)]

    if not july_data_after.empty:
      
        july_mean_after = july_data_after['Production(Wh)'].mean()
        
        # Valeurs manquantes remplies avec production moyenne du mois de juillet de l'année suivante
        df.loc[july_data.index, 'Production(Wh)'] = df.loc[july_data.index, 'Production(Wh)'].fillna(july_mean_after)
    else:
        print(f"No data available for July {target_year + 1} to impute July {target_year}")

# Imputation pour 2021
impute_july_with_next_year(df, target_year=2021)


#Remplacer tout le mois de juillet 2020 par celui de 2021
# Filtrer les données de juillet 2020 et juillet 2021
july_2020 = df[(df['Datetime'].dt.year == 2020) & (df['Datetime'].dt.month == 7)]
july_2021 = df[(df['Datetime'].dt.year == 2021) & (df['Datetime'].dt.month == 7)]

# Vérifier si les deux mois ont le même nombre de jours et donc de lignes
if len(july_2020) == len(july_2021):
    # Remplacer les valeurs de production de juillet 2020 par celles de juillet 2021
    df.loc[july_2020.index, 'Production'] = july_2021['Production'].values
else:
    print("Les données de juillet 2020 et juillet 2021 ne correspondent pas en longueur.")