"""
Módulo de limpieza y preparación de datos
Contiene funciones para limpiar y estandarizar datos de CSV
"""

import pandas as pd # type: ignore
import numpy as np # type: ignore


def cargar_datos(ruta_archivo):
    """
    Carga datos desde un archivo CSV
    
    Args:
        ruta_archivo (str): Ruta al archivo CSV
        
    Returns: 
        pd.DataFrame: DataFrame con los datos cargados
    """
    try:
        df = pd.read_csv(ruta_archivo, encoding='utf-8')
        print(f"✅ Datos cargados exitosamente:  {df.shape[0]} filas, {df.shape[1]} columnas")
        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {ruta_archivo}")
        return None
    except Exception as e:
        print(f"❌ Error al cargar datos: {e}")
        return None


def manejar_valores_nulos(df, estrategia='eliminar', columnas=None):
    """
    Maneja valores nulos en el DataFrame
    
    Args: 
        df (pd.DataFrame): DataFrame a procesar
        estrategia (str): 'eliminar', 'rellenar_media', 'rellenar_moda', 'rellenar_cero'
        columnas (list): Lista de columnas específicas a procesar (None = todas)
        
    Returns: 
        pd.DataFrame: DataFrame con valores nulos manejados
    """
    df_limpio = df.copy()
    
    # Mostrar información sobre valores nulos
    nulos_antes = df_limpio.isnull().sum()
    print("\n📊 Valores nulos por columna (antes):")
    print(nulos_antes[nulos_antes > 0])
    
    if estrategia == 'eliminar': 
        df_limpio = df_limpio.dropna(subset=columnas)
        print(f"✅ Filas eliminadas: {len(df) - len(df_limpio)}")
        
    elif estrategia == 'rellenar_media':
        columnas_numericas = df_limpio.select_dtypes(include=[np.number]).columns
        if columnas:
            columnas_numericas = [col for col in columnas if col in columnas_numericas]
        df_limpio[columnas_numericas] = df_limpio[columnas_numericas].fillna(
            df_limpio[columnas_numericas].mean()
        )
        print("✅ Valores nulos rellenados con la media")
        
    elif estrategia == 'rellenar_moda':
        cols_procesar = columnas if columnas else df_limpio. columns
        for col in cols_procesar: 
            if df_limpio[col].isnull().any():
                moda = df_limpio[col].mode()[0] if not df_limpio[col].mode().empty else 'N/A'
                df_limpio[col]. fillna(moda, inplace=True)
        print("✅ Valores nulos rellenados con la moda")
        
    elif estrategia == 'rellenar_cero':
        columnas_numericas = df_limpio.select_dtypes(include=[np.number]).columns
        if columnas:
            columnas_numericas = [col for col in columnas if col in columnas_numericas]
        df_limpio[columnas_numericas] = df_limpio[columnas_numericas].fillna(0)
        print("✅ Valores nulos rellenados con ceros")
    
    # Mostrar información después
    nulos_despues = df_limpio.isnull().sum()
    print("\n📊 Valores nulos por columna (después):")
    print(nulos_despues[nulos_despues > 0] if nulos_despues. sum() > 0 else "No hay valores nulos")
    
    return df_limpio


def estandarizar_texto(df, columnas_texto):
    """
    Estandariza columnas de texto:  convierte a minúsculas y elimina espacios extra
    
    Args:
        df (pd. DataFrame): DataFrame a procesar
        columnas_texto (list): Lista de nombres de columnas de texto
        
    Returns: 
        pd.DataFrame: DataFrame con texto estandarizado
    """
    df_limpio = df. copy()
    
    for columna in columnas_texto: 
        if columna in df_limpio.columns:
            # Convertir a string primero para evitar errores
            df_limpio[columna] = df_limpio[columna].astype(str)
            # Convertir a minúsculas
            df_limpio[columna] = df_limpio[columna].str.lower()
            # Eliminar espacios al inicio y final
            df_limpio[columna] = df_limpio[columna].str.strip()
            # Eliminar espacios múltiples
            df_limpio[columna] = df_limpio[columna].str.replace(r'\s+', ' ', regex=True)
            print(f"✅ Texto estandarizado en columna:  {columna}")
        else:
            print(f"⚠️  Advertencia: Columna '{columna}' no encontrada")
    
    return df_limpio


def limpiar_moneda(df, columnas_moneda, simbolo='$'):
    """
    Limpia símbolos de moneda y convierte a float
    Función específica para datos financieros
    
    Args: 
        df (pd.DataFrame): DataFrame a procesar
        columnas_moneda (list): Lista de columnas con valores monetarios
        simbolo (str): Símbolo de moneda a eliminar (default: '$')
        
    Returns:
        pd.DataFrame: DataFrame con valores numéricos limpios
    """
    df_limpio = df.copy()
    
    for columna in columnas_moneda:
        if columna in df_limpio.columns:
            # Convertir a string primero
            df_limpio[columna] = df_limpio[columna].astype(str)
            # Eliminar símbolo de moneda y comas
            df_limpio[columna] = df_limpio[columna].str.replace(simbolo, '', regex=False)
            df_limpio[columna] = df_limpio[columna]. str.replace(',', '', regex=False)
            df_limpio[columna] = df_limpio[columna]. str.strip()
            # Convertir a float
            df_limpio[columna] = pd.to_numeric(df_limpio[columna], errors='coerce')
            print(f"✅ Moneda limpiada en columna: {columna}")
        else:
            print(f"⚠️  Advertencia: Columna '{columna}' no encontrada")
    
    return df_limpio


def detectar_duplicados(df):
    """
    Detecta y muestra información sobre filas duplicadas
    
    Args:
        df (pd.DataFrame): DataFrame a analizar
        
    Returns: 
        pd.DataFrame: DataFrame sin duplicados
    """
    duplicados = df. duplicated().sum()
    print(f"\n📊 Filas duplicadas encontradas: {duplicados}")
    
    if duplicados > 0:
        df_limpio = df. drop_duplicates()
        print(f"✅ Duplicados eliminados: {duplicados}")
        return df_limpio
    
    return df


def resumen_datos(df):
    """
    Muestra un resumen completo del DataFrame
    
    Args: 
        df (pd.DataFrame): DataFrame a resumir
    """
    print("\n" + "="*60)
    print("📊 RESUMEN DE DATOS")
    print("="*60)
    print(f"\n🔢 Dimensiones:  {df.shape[0]} filas × {df.shape[1]} columnas")
    print(f"\n📋 Columnas: {list(df.columns)}")
    print("\n📈 Tipos de datos:")
    print(df.dtypes)
    print("\n📊 Estadísticas descriptivas:")
    print(df.describe())
    print("\n🔍 Primeras 5 filas:")
    print(df.head())
    print("="*60 + "\n")
