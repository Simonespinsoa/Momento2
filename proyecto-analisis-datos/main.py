


import sys
import os


if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#
sys.path.insert(0, os.path.join(os. path.dirname(__file__), 'src'))

from limpieza_datos import (
    cargar_datos,
    manejar_valores_nulos,
    estandarizar_texto,
    limpiar_moneda,
    detectar_duplicados,
    resumen_datos
)
from analisis import (
    filtrar_datos,
    agrupar_datos,
    top_n_valores
)


def main():
    """
    Función principal que ejecuta el análisis de datos
    """
    print("="*60)
    print("ANALISIS DE DATOS - PROYECTO PYTHON - MOMENTO 2")
    print("="*60)
    
    
    print("\n[PASO 1] Cargando datos...")
    import os
    ruta_csv = os.path.join(os.path.dirname(__file__), 'data', 'datos.csv')
    df = cargar_datos(ruta_csv)
    
    if df is None or df.empty:
        print("[ERROR] No se pudieron cargar los datos.")
        print("Asegurate de tener un archivo 'data/datos.csv'")
        sys.exit(1)
    
   
    resumen_datos(df)
    
    
    print("\n[PASO 2] Limpiando datos...")
    
    
    df = detectar_duplicados(df)
    
    
    df = manejar_valores_nulos(df, estrategia='eliminar')
    
    
    print("\n[PASO 2] Limpiando datos...")
    
    
    df = detectar_duplicados(df)
    
 
    df = manejar_valores_nulos(df, estrategia='eliminar')
    
    
    print("\n[OK] Limpieza completada!")
    
    
    print("\n[PASO 3] Realizando análisis...")
    
    
    print("\n" + "-"*60)
    print("[PREGUNTA 1] Filtrado de datos")
    print("-"*60)
    print("Aqui puedes filtrar datos segun condiciones")
    
    
    
    print("\n" + "-"*60)
    print("[PREGUNTA 2] Agrupacion de datos (groupby)")
    print("-"*60)
    print("Aqui puedes agrupar y calcular estadisticas")
    
    
    
    print("\n" + "-"*60)
    print("[PREGUNTA 3] Top N valores")
    print("-"*60)
    print("Aqui puedes obtener los mayores o menores valores")
    
    
    print("\n" + "="*60)
    print("[OK] ANALISIS COMPLETADO EXITOSAMENTE")
    print("="*60)


if __name__ == "__main__":
    main()
