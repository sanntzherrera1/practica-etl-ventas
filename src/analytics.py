#Genero unas metricas para el df y lo devuelvo en csv como ej
# Una metrica para el análisis RFM (Recency, Frequency, Monetary)

import pandas as pd
import datetime as dt

def analizar_rfm(df_limpio):
    """
    Calcula el RFM (Recencia, Frecuencia, Valor Monetario) por cliente.
    """
    if df_limpio is not None:
        print("Entrando al calculo matriz RFM...")

        #Preparo y armo una copia para facilidad
        df = df_limpio.copy()
        
        # Calculamos el total de monto por fila
        df['total_venta'] = df['cantidad'] * df['precio_unitario']

        # Definimos la fecha de referencia ("Hoy")
        # dataset + 1 día para que nadie tenga recencia 0
        fecha_actual = df['fecha'].max() + dt.timedelta(days=1)

        # Agrupamos por Cliente (RFM)
        rfm = df.groupby('cliente_email').agg({
            'fecha': lambda x: (fecha_actual - x.max()).days,  # R: Días desde la última compra
            'cliente_email': 'count',                           # F: Cuántas veces compró
            'total_venta': 'sum'                                # M: Cuánto gastó en total
        })

        # 4. Renombramos columnas para que quede prolijo
        rfm.rename(columns={
            'fecha': 'recency_dias',
            'cliente_email': 'frequency_cantidad',
            'total_venta': 'monetary_dinero'
        }, inplace=True)

        #Ordenamos por los que más gastan
        rfm = rfm.sort_values(by='monetary_dinero', ascending=False)

        print("Matriz RFM generada!")
        return rfm

    else:
        return None

