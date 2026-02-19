import pandas as pd
from sodapy import Socrata

def consultar_covid(departamento, limite):
    try:
        client = Socrata("www.datos.gov.co", None)

        if int(limite) > 1000:
            print("El límite máximo permitido es 1000")
            return None

        results = client.get(
            "gt2j-8ykr",
            limit=int(limite),
            where=f"departamento_nom='{departamento.upper()}'"
        )

        if not results:
            print("No se encontraron datos para ese departamento.")
            return None

        df = pd.DataFrame.from_records(results)

        # Crear columna pais_procedencia segura
        if "pais_viajo_1_nom" not in df.columns:
            df["pais_viajo_1_nom"] = "No reportado"

        columnas = [
            "ciudad_municipio_nom",
            "departamento_nom",
            "edad",
            "fuente_tipo_contagio",
            "estado",
            "pais_viajo_1_nom"
        ]

        df_filtrado = df[columnas].fillna("No reportado")

        return df_filtrado

    except Exception as e:
        print("Error en la consulta:", e)
        return None
