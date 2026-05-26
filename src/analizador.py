import argparse
from email.mime import text
from py_compile import main

# =========================================
# Lectura del archivo fasta y guardado de secuencias en listas de tuplas (encabezado, secuencia)
# =========================================
# =========================================
# Responsabilidad: leer secuencias desde archivo fasta y almacenarlas en una lista de tuplas (encabezado, secuencia)
# Entrada: archivo
# Salida: lista de tuplas de las secuencias
# =========================================


def parsear_argumentos():
    """Lee los argumentos de la línea de comandos.
    Returns:
    argparse.Namespace: Objeto con los argumentos leídos"""
    parser = argparse.ArgumentParser(
        description="Generar estadísticas de secuencias a partir de un archivo fasta"
    )
    parser.add_argument(
        "-i",
        "--input",
        help="Ruta del archivo FASTA de entrada ",
        required=True,
    )
    parser.add_argument(
        "-o", "--output", help="Ruta del archivo TSV de salida", required=True
    )

    parser.add_argument(
        "--min_len",
        type=int,
        default=0,
        help="Longitud mínima permitida de las secuencias",
    )

    parser.add_argument(
        "--max_len",
        type=int,
        default=0,
        help="Longitud máxima permitida de las secuencias",
    )

    parser.add_argument(
        "--min_gc",
        type=int,
        default=0,
        help="Contenido GC mínimo permitido de las secuencias",
    )
    parser.add_argument(
        "--max_gc",
        type=int,
        default=0,
        help="Contenido GC máximo permitido de las secuencias",
    )

    return parsear_argumentos()

# =========================================
#lectura del archivo fasta y guardado de secuencias en listas de tuplas (encabezado, secuencia)
# =========================================
# =========================================
# Responsabilidad: Leer secuencias desde archivo fasta y almacenarlas en una lista de tuplas (encabezado, secuencia)
# Entrada: archivo
# Salida: lista de tuplas de las secuencias
# =========================================
def calcular_gc(secuencia):

def leer_fasta(ruta):
    secuencias = []  # Lista para almacenar las secuencias y sus encabezados
    encabezado_actual = None  # Variable para almacenar el encabezado actual
    secuencia_actual = ""  # Variable para acumular la secuencia actual

    with open(ruta, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()  # Limpiar espacios y saltos de línea

            if linea.startswith(">"):  # Si la línea es un encabezado
                if (
                    encabezado_actual is not None
                ):  # Si ya teníamos una secuencia anterior
                    secuencias.append(
                        (encabezado_actual, secuencia_actual)
                    )  # Guardarla en la lista

                encabezado_actual = linea[1:]  # Guardar el nuevo encabezado (sin ">")
                secuencia_actual = ""  # Reiniciar la secuencia actual
            else:
                secuencia_actual += linea  # Agregar esa línea a la secuencia actual

        # Al terminar el archivo, guardar la última secuencia
        if encabezado_actual is not None:
            secuencias.append((encabezado_actual, secuencia_actual))

    return leer_fasta(ruta)



# =========================================
# Cálculo de contenido de gc (secuencia)
# =========================================
# =========================================
# Responsabilidad: calcular contenido gc de una secuencia dada
# Entrada: secuencia
# Salida: contenido gc
# =========================================
def calcular_gc(secuencia):
    longitud = len(secuencia)  # Calcular la longitud de la secuencia
    g_count = secuencia.count("G")  # Contar el número de G
    c_count = secuencia.count("C")  # Contar el número de C
    gc_content = (
        (g_count + c_count) / longitud if longitud > 0 else 0
    )  # Calcular el contenido GC

    return gc_content

# =========================================
# Cálculo de estadísticas para tuplas (encabezado, secuencia)
# =========================================
# =========================================
# Responsabilidad: calcular estadísticas para una lista de tuplas (encabezado, secuencia)
# Entrada: lista de tuplas (encabezado, secuencia)
# Salida: lista de tuplas con estadísticas
# =========================================
def calcular_estadisticas(
    encabezado, secuencia
):  # Esta función reunirá las estadísticas de una secuencia en un diccionario.
    estadisticas = []  # Lista para almacenar las estadísticas

    for encabezado, secuencia in secuencias:
        encabezado = encabezado.strip()  # Limpiar espacios en el encabezado
        longitud = len(secuencia)
        gc_content = calcular_gc(secuencia)

        estadisticas.append((encabezado, longitud, gc_content))

    return calcular_estadisticas(encabezado, secuencia)


# =========================================
# FILTROS para las estadísticas de las secuencias
# =========================================
# =========================================
# Responsabilidad: decidir si una secuencia debe conservarse según los filtros indicados por el usuario
# Entrada: estadísticas de una secuencia y argumentos de los filtros
# Salida: booleano indicando si la secuencia pasa los filtros o no
# =========================================
def pasa_filtros(estadisticas, args):   
    if args.min_len > 0 and estadisticas[1] < args.min_len:
        return False    
    if args.max_len > 0 and estadisticas[1] > args.max_len:
        return False
    if args.min_gc > 0 and estadisticas[2] < args.min_gc:
        return False
    if args.max_gc > 0 and estadisticas[2] > args.max_gc:
        return False 
    
    return True #si todas cumplen con false, entonces pasa los filtros        

# =========================================
# Escribir resultados en un archivo TSV
# =========================================
# =========================================
# Responsabilidad: escribir resultados en un archivo TSV con encabezados y estadísticas de las secuencias que pasaron los filtros
# Entrada: estadísticas de las secuencias que pasaron los filtros y ruta del archivo de salida
# Salida: archivo TSV con los resultados
# =========================================

def escribir_resultados(stats,ruta):
##Esta función escribirá el archivo final en formato TSV.
#Debe incluir una primera línea con los nombres de las columnas
    with open(ruta, "w") as archivo:
        archivo.write("Encabezado\tLongitud\tGC_Content\n")  # Escribir encabezado
        for estad in stats:
            archivo.write(f"{estad[0]}\t{estad[1]}\t{estad[2]:.2f}\n")  # Escribir cada estadística
#La función `main()` será la encargada de coordinar todo:

#
#leer argumentos
#leer FASTA
#calcular estadísticas
#filtrar resultados
#escribir archivo TSV

main()
args = parsear_argumentos()  # Leer argumentos
secuencias = leer_fasta(args.input)  # Leer secuencias del archivo
estadisticas = calcular_estadisticas(secuencias)  # Calcular estadísticas
resultados_filtrados = [
    estad for estad in estadisticas if pasa_filtros(estad, args)
    ]  # Filtrar resultados
escribir_resultados(resultados_filtrados, args.output)  # Escribir resultados en archivo TSV    
#mostrar resumen
print(f"Resultados filtrados: {len(resultados_filtrados)}")