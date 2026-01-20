import pandas as pd
import os 
import extract as exc
import transform as tr
import load as ld
import analytics as an

def run_main_etl():
    print("INICIANDO PROCESO ETL \n")

    #Extraccion/Lectura del csv
    print("[EXTRACT] Leyendo archivo...")
    # Ajusta esta ruta según dónde esté tu archivo real
    route = '../data/raw/data_ventas.csv' 
    df_raw = exc.ver_data(route)

    #Manejo de error por extraccion
    if df_raw is None:
        print("ERROR en Extracción. Se cancela el proceso.")
        return

    #Transformacion del dataframe
    print("\n[TRANSFORM] Limpiando datos...")
    # Le pasamos el resultado del paso 1
    df_clean = tr.transform_data(df_raw)

    #Manejo de error por transformacion
    if df_clean is None:
        print("ERROR en Transformación. Se cancela el proceso.")
        return
    
    #LOAD
    print("\n[LOAD] Guardando archivos...")
    # Guardamos la data limpia completa
    ld.load_data_csv(df_clean, 'ventas_limpias.csv')
    
    #Genero el analisis de metrica rfm
    print("\n [ANALYSIS] Generando matriz RFM...")
    df_rfm = an.analizar_rfm(df_clean)

    # Guardamos el análisis RFM
    if df_rfm is not None:
        #acordarse - reset_index() para que el email se guarde como columna y no como índice
        ld.load_data_csv(df_rfm.reset_index(), 'reporte_rfm_clientes.csv')


    print("\nETL TERMINADO CON ÉXITO! ")

#Ejecucion de main
if __name__ == "__main__":
    run_main_etl()






