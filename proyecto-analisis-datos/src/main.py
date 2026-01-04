

import sys
from src.limpieza_datos import (
    cargar_datos,
    manejar_valores_nulos,
    estandarizar_texto,
    limpiar_moneda,
    detectar_duplicados,
    resumen_datos
)
from src.analisis import (
    filtrar_datos,
    agrupar_datos,
    combinar_dataframes,
    top_n_valores
)


def main():
    
    print("="*60)
    print("🚀 ANÁLISIS DE DATOS - PROYECTO PYTHON")
    print("="*60)
    
    # 1. CARGAR DATOS
    print("\n📂 PASO 1: Cargando datos...")
    df = cargar_datos('data/datos.csv')
    
    if df is None:
        print("❌ No se pudieron cargar los datos.  Terminando programa.")
        sys.exit(1)
    
    # Mostrar resumen inicial
    resumen_datos(df)
    
    # 2. LIMPIEZA DE DATOS
    print("\n🧹 PASO 2: Limpiando datos...")
    
    # Detectar duplicados
    df = detectar_duplicados(df)
    
    # Manejar valores nulos (ajustar estrategia según tu caso)
    df = manejar_valores_nulos(df, estrategia='eliminar')
    
    # Estandarizar texto (ajustar columnas según tu CSV)
    # Ejemplo: columnas_texto = ['nombre', 'categoria', 'descripcion']
    # df = estandarizar_texto(df, columnas_texto)
    
    # Limpiar moneda (si aplica)
    # Ejemplo: columnas_moneda = ['precio', 'costo']
    # df = limpiar_moneda(df, columnas_moneda, simbolo='$')
    
    print("\n✅ Limpieza completada!")
    
    # 3. ANÁLISIS DE DATOS
    print("\n📊 PASO 3: Realizando análisis...")
    
    # PREGUNTA 1: Filtrado de datos
    print("\n" + "-"*60)
    print("❓ PREGUNTA 1: [Tu pregunta específica sobre filtrado]")
    print("-"*60)
    # Ejemplo: df_filtrado = filtrar_datos(df, {'categoria': 'electronica'})
    # print(df_filtrado)
    
    # PREGUNTA 2: Agrupación de datos
    print("\n" + "-"*60)
    print("❓ PREGUNTA 2: [Tu pregunta sobre agrupación]")
    print("-"*60)
    # Ejemplo: df_agrupado = agrupar_datos(df, 'categoria', 'precio', 'mean')
    # print(df_agrupado)
    
    # PREGUNTA 3: Top N valores
    print("\n" + "-"*60)
    print("❓ PREGUNTA 3: [Tu pregunta sobre valores máximos/mínimos]")
    print("-"*60)
    # Ejemplo: top_productos = top_n_valores(df, 'ventas', n=10)
    # print(top_productos)
    
    # PREGUNTA 4: Análisis adicional
    print("\n" + "-"*60)
    print("❓ PREGUNTA 4: [Tu pregunta personalizada]")
    print("-"*60)
    # Tu código de análisis aquí
    
    print("\n" + "="*60)
    print("✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("="*60)


if __name__ == "__main__":
    main()