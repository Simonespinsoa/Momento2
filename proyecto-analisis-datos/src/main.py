


import sys
import os

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


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
    
    # 1. CARGAR DATOS
    print("\n[PASO 1] Cargando datos...")
    df = cargar_datos('data/datos.csv')
    
    if df is None:
        print("[ERROR] No se pudieron cargar los datos.")
        print("Asegurate de tener un archivo 'data/datos.csv'")
        sys.exit(1)
    
    
    resumen_datos(df)
    
    # 2. LIMPIEZA DE DATOS
    print("\n[PASO 2] Limpiando datos...")
    
    # Detectar duplicados
    df = detectar_duplicados(df)
    
  
    df = manejar_valores_nulos(df, estrategia='eliminar')
    
    
    
    print("\n[OK] Limpieza completada!")
    
    # 3. ANÁLISIS DE DATOS
    print("\n[PASO 3] Realizando análisis...")
    
    # PREGUNTA 1: Filtrado
    print("\n" + "-"*60)
    print("[PREGUNTA 1] Filtrado de datos")
    print("-"*60)
    print("Aqui puedes filtrar datos segun condiciones")
    
    
    # PREGUNTA 2: Agrupación
    print("\n" + "-"*60)
    print("[PREGUNTA 2] Agrupacion de datos (groupby)")
    print("-"*60)
    print("Aqui puedes agrupar y calcular estadisticas")
   
    
    # PREGUNTA 3: Top valores
    print("\n" + "-"*60)
    print("[PREGUNTA 3] Top N valores")
    print("-"*60)
    print("Aqui puedes obtener los mayores o menores valores")
   
    
    print("\n" + "="*60)
    print("[OK] ANALISIS COMPLETADO EXITOSAMENTE")
    print("="*60)


if __name__ == "__main__":
    main()