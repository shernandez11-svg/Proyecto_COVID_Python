def pedir_datos():
    departamento = input("Ingrese el nombre del departamento: ")
    limite = input("Ingrese el número de registros a consultar: ")
    return departamento, limite


def mostrar_resultados(df):
    if df is None or df.empty:
        print("No hay resultados para mostrar.")
        return

    print("\nResultados de la consulta:\n")

    for index, row in df.iterrows():
        print(
            "Ciudad: {:20} | Departamento: {:15} | Edad: {:3} | Tipo: {:15} | Estado: {:15} | País: {:15}".format(
                str(row["ciudad_municipio_nom"]),
                str(row["departamento_nom"]),
                str(row["edad"]),
                str(row["fuente_tipo_contagio"]),
                str(row["estado"]),
                str(row["pais_viajo_1_nom"])
            )
        )
