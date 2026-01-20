import pandas as pd
import os

def load_data_csv(dataframe,nombre_archivo='ventas_limpias.csv'):
    
    if dataframe is not None:
        # Definimos la carpeta de destino
        carpeta = '../data/output'
        
        # Creamos la carpeta si no existe
        os.makedirs(carpeta, exist_ok=True)
        
        # Creamos la ruta completa
        ruta_completa = os.path.join(carpeta,nombre_archivo )
        
        # Guardamos el archivo
        dataframe.to_csv(ruta_completa, index=False, encoding='utf-8')
        
        print(f"Archivo guardado en: {ruta_completa}")
    else:
        print("No se pudo guardar el dataframe")

if __name__ == "__main__":
    print("Modulo para probar si funciona load")
    #Creacion de datos falsos para unit test

    datos_falsos = {
        'fecha': ['2025-01-01', '2025-01-02'],
        'producto': ['Product1', 'Product2'],
        'cantidad': [10, 20]
    }
    df_test = pd.DataFrame(datos_falsos)

    #Si funciona me retorna un csv nuevo
    load_data_csv(df_test, 'test_de_carga.csv')
