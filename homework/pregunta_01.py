"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_02():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

import pandas as pd
from datetime import datetime

def validar_formato_fecha(fecha):
    """
    Valida y transforma las fechas al formato DD/MM/YYYY.
    Si el formato no es válido, retorna el valor original.
    """
    try:
        # Intentar convertir al formato DD/MM/YYYY
        fecha_validada = datetime.strptime(fecha, "%d/%m/%Y")
        return fecha_validada.strftime("%d/%m/%Y")
    except ValueError:
        try:
            # Intentar convertir al formato YYYY/MM/DD
            fecha_validada = datetime.strptime(fecha, "%Y/%m/%d")
            return fecha_validada.strftime("%d/%m/%Y")
        except ValueError:
            # Si no coincide con ninguno de los formatos, retornar el valor original
            return fecha
        
def pregunta_01():

    input_file = "files/input/solicitudes_de_credito.csv"
    output_file = "files/output/solicitudes_de_credito.csv"
    """
    Función para limpiar un archivo CSV de solicitudes de crédito.
    
    - Convierte los datos a minúsculas.
    - Elimina duplicados.
    - Elimina filas con valores vacíos.
    - Guarda el archivo limpio en la ruta especificada.
    
    Parámetros:
    - input_file: Ruta del archivo de entrada.
    - output_file: Ruta del archivo de salida.
    """
    # Leer el archivo CSV
    dfi = pd.read_csv(input_file, sep=";")
    df = pd.read_csv(input_file, sep=";")

    #Quitar primera columna de indice
    df = df.drop(df.columns[0], axis=1)

    # Convertir todas las columnas y valores a minúsculas
    df.columns = df.columns.str.lower()
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    #Reemplazar _ por espacio
    df = df.apply(lambda col: col.str.replace('_', ' ') if col.dtype == 'object' else col)

    #Reemplazar - por espacio
    df = df.apply(lambda col: col.str.replace('-', ' ') if col.dtype == 'object' else col)

    #Quitar espacios al inicio y al final
    df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    #Convierte los montos a numero entero
    df['monto_del_credito'] = df['monto_del_credito'].replace({'\$': '', ',': '', '\$ ': ''}, regex=True)
    df['monto_del_credito'] = pd.to_numeric(df['monto_del_credito'], errors='coerce').fillna(0).astype(int)

    #df['línea_credito'] = df['línea_credito'].replace('soli diaria', 'solidaria')
    #df['barrio'] = df['barrio'].replace('bel¿n', 'belen')
    #df['barrio'] = df['barrio'].replace('antonio nari¿o', 'antonio nariño')

    # Validar y transformar fechas al formato DD/MM/YYYY
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(validar_formato_fecha)



    # Eliminar duplicados
    df = df.drop_duplicates()

    # Eliminar filas con valores vacíos en cualquier columna
    df = df.dropna()

    # Guardar el archivo limpio
    df.to_csv(output_file, sep=";", index=False)

    dfbarrio = df['barrio'].value_counts().reset_index()
    #dfbarrio.to_csv('files/output/barrios.csv', sep=";", index=False)
    #df.to_csv('files/output/salida_solicitudes_de_credito.csv', sep=";", index=False)
    

    return df.sexo.value_counts()
    
#== [6617, 3589]
#df.comuna_ciudadano.value_counts().to_list()
#sorted(df['fecha_de_beneficio'].dropna().unique())


if __name__ == "__main__":
    # Rutas de entrada y salida


    # Llamar a la función
    print(pregunta_01())
