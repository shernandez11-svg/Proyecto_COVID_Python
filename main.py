from ui import pedir_datos, mostrar_resultados
from api import consultar_covid

def main():
    departamento, limite = pedir_datos()
    datos = consultar_covid(departamento, limite)
    mostrar_resultados(datos)

if __name__ == "__main__":
    main()
