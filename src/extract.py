import pandas as pd
import os 

def ver_data(archivo_csv):
    #Manejo de error, si existe o no el csv/ruta
    if os.path.exists(archivo_csv):
        df_ventas = pd.read_csv(archivo_csv)

        return df_ventas
    else:
        print(f"No encontre el csv: {archivo_csv}")
        return None
    