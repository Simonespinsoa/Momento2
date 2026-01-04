

import pandas as pd 


def filtrar_datos(df, condiciones):
    """
    Filtra datos según condiciones especificadas
    
    Args: 
        df (pd.DataFrame): DataFrame a filtrar
        condiciones (dict): Diccionario con condiciones {columna: valor}
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    df_filtrado = df.copy()
    
    for columna, valor in condiciones.items():
        if columna in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado[columna] == valor]
            print(f" Filtrado por {columna} = {valor}:  {len(df_filtrado)} filas")
        else:
            print(f"  Advertencia: Columna '{columna}' no encontrada")
    
    return df_filtrado


def agrupar_datos(df, columna_grupo, columna_agregacion, operacion='sum'):
    """
    Agrupa datos y realiza operaciones de agregación
    
    Args: 
        df (pd.DataFrame): DataFrame a agrupar
        columna_grupo (str): Columna para agrupar
        columna_agregacion (str): Columna a agregar
        operacion (str): 'sum', 'mean', 'count', 'max', 'min'
        
    Returns:
        pd.DataFrame: DataFrame agrupado
    """
    operaciones = {
        'sum': 'suma',
        'mean': 'promedio',
        'count':  'conteo',
        'max': 'máximo',
        'min': 'mínimo'
    }
    
    if operacion in operaciones:
        resultado = df.groupby(columna_grupo)[columna_agregacion].agg(operacion).reset_index()
        resultado.columns = [columna_grupo, f'{operaciones[operacion]}_{columna_agregacion}']
        print(f"\n Agrupación por '{columna_grupo}' - {operaciones[operacion]} de '{columna_agregacion}'")
        return resultado
    else:
        print(f" Operación '{operacion}' no válida")
        return df


def combinar_dataframes(df1, df2, columna_union, tipo='inner'):
    """
    Combina dos DataFrames (merge/join)
    
    Args:
        df1 (pd. DataFrame): Primer DataFrame
        df2 (pd.DataFrame): Segundo DataFrame
        columna_union (str): Columna común para la unión
        tipo (str): 'inner', 'left', 'right', 'outer'
        
    Returns:
        pd.DataFrame: DataFrame combinado
    """
    try:
        df_combinado = pd.merge(df1, df2, on=columna_union, how=tipo)
        print(f"\n DataFrames combinados ({tipo} join) en columna '{columna_union}'")
        print(f"   Resultado: {len(df_combinado)} filas")
        return df_combinado
    except Exception as e:
        print(f" Error al combinar DataFrames: {e}")
        return None


def top_n_valores(df, columna, n=10, ascendente=False):
    """
    Obtiene los top N valores de una columna
    
    Args:
        df (pd.DataFrame): DataFrame a analizar
        columna (str): Columna a ordenar
        n (int): Número de registros a retornar
        ascendente (bool): True para menores, False para mayores
        
    Returns:
        pd.DataFrame: Top N registros
    """
    top = df.nlargest(n, columna) if not ascendente else df.nsmallest(n, columna)
    orden = "menores" if ascendente else "mayores"
    print(f"\n Top {n} {orden} valores de '{columna}'")
    return top
