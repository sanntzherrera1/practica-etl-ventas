import pandas as pd
import extract as exc


def transform_data(dataframe):

    if dataframe is not None:
        
        print("--- Data Original ---")
        print(dataframe)


        # Primero unificamos separadores, luego convertimos
        dataframe['fecha'] = dataframe['fecha'].astype(str).str.replace('-', '/')
        dataframe['fecha'] = pd.to_datetime(dataframe['fecha'], errors='coerce', dayfirst=True, format='mixed')

        # Agregamos .strip() por seguridad 
        dataframe['producto'] = dataframe['producto'].str.title().str.strip()

        #Elimino duplicados
        dataframe.drop_duplicates(keep='first', inplace=True)

        # Arreglamos error pasando de string a numero
        dataframe['cantidad'] = dataframe['cantidad'].replace({'uno': 1})
        #  Forzamos conversión a enteros
        dataframe['cantidad'] = pd.to_numeric(dataframe['cantidad'], errors='coerce')

        dataframe['cantidad'] = dataframe['cantidad'].fillna(0).astype(int)

        # Limpieza de nulos 
        dataframe['precio_unitario'] = pd.to_numeric(dataframe['precio_unitario'], errors='coerce').fillna(0)
        dataframe['cliente_email'] = dataframe['cliente_email'].fillna('No tiene mail')

        # Retorno final
        print("\n--- Data Transformada ---")
        print(dataframe)
        
        return dataframe
    else:
        
        print("Hubo un error con el archivo")


if __name__ == "__main__":
    #Se ejecuta si no uso main.py
    print("---Transform data---")
    route = '../data/raw/data_ventas.csv'
    df = exc.ver_data(route)
    transform_data(df)
