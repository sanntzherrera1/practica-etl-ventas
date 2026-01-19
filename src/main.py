import pandas as pd
import extract as exc

route = ('../data/raw/data_ventas.csv')

new_df_ventas = exc.ver_data(route)

if new_df_ventas is not None:
    print("\n Impresion del csv:")
    print(new_df_ventas.head(5))






