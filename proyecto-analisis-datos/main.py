# -*- coding: utf-8 -*-
"""
Script principal para análisis de datos
Proyecto:  Análisis de Datos con Python - Momento 2
Autor: Simon Espinosa
Fecha:  Enero 2026
"""

import sys
import os

# Configurar encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Agregar src al path
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
    import os
    ruta_csv = os.path.join(os.path.dirname(__file__), 'data', 'datos.csv')
    df = cargar_datos(ruta_csv)
    
    if df is None or df.empty:
        print("[ERROR] No se pudieron cargar los datos.")
        print("Asegurate de tener un archivo 'data/datos.csv'")
        sys.exit(1)
    
    # Mostrar resumen inicial
    resumen_datos(df)
    
    # 2. LIMPIEZA DE DATOS
    print("\n[PASO 2] Limpiando datos...")
    
    # Detectar duplicados
    df = detectar_duplicados(df)
    
    # Manejar valores nulos
    df = manejar_valores_nulos(df, estrategia='eliminar')
    
    # 2. LIMPIEZA DE DATOS
    print("\n[PASO 2] Limpiando datos...")
    
    # Detectar duplicados
    df = detectar_duplicados(df)
    
    # Manejar valores nulos
    df = manejar_valores_nulos(df, estrategia='eliminar')
    
    # Ejemplo:  Estandarizar texto
    # columnas_texto = ['nombre', 'ciudad']
    # df = estandarizar_texto(df, columnas_texto)
    
    # Ejemplo: Limpiar moneda
    # columnas_moneda = ['salario']
    # df = limpiar_moneda(df, columnas_moneda, simbolo='$')
    
    print("\n[OK] Limpieza completada!")
    
    # 3. ANÁLISIS DE DATOS
    print("\n[PASO 3] Realizando análisis...")
    
    # PREGUNTA 1: Filtrado
    print("\n" + "-"*60)
    print("[PREGUNTA 1] Filtrado de datos")
    print("-"*60)
    print("Aqui puedes filtrar datos segun condiciones")
    # Ejemplo: df_filtrado = filtrar_datos(df, {'ciudad': 'bogota'})
    
    # PREGUNTA 2: Agrupación
    print("\n" + "-"*60)
    print("[PREGUNTA 2] Agrupacion de datos (groupby)")
    print("-"*60)
    print("Aqui puedes agrupar y calcular estadisticas")
    # Ejemplo: df_agrupado = agrupar_datos(df, 'ciudad', 'salario', 'mean')
    
    # PREGUNTA 3: Top valores
    print("\n" + "-"*60)
    print("[PREGUNTA 3] Top N valores")
    print("-"*60)
    print("Aqui puedes obtener los mayores o menores valores")
    # Ejemplo: top_5 = top_n_valores(df, 'salario', n=5)
    
    print("\n" + "="*60)
    print("[OK] ANALISIS COMPLETADO EXITOSAMENTE")
    print("="*60)


if __name__ == "__main__":
    main()
