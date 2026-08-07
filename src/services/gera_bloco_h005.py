import pandas as pd
from pandas import DataFrame
from datetime import date

def adiciona_h005(
            df: DataFrame,
            coluna_valor_total: str,
            data_inventario: date,
            motivo: str = "01"
        ) -> DataFrame:
        valor_inventario = round(df[coluna_valor_total].sum(), 2)

        h005 = {
            "REG": "H005",
            "COD_ITEM": data_inventario.strftime("%d%m%Y"),
            "UNID": valor_inventario,
            "QTD": motivo
        }

        df_h005 = pd.DataFrame([h005])
        return pd.concat([df_h005, df], ignore_index=True)