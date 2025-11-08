import sqlite3
import pandas as pd
from pathlib import Path


class Bdatos:
    """
    Clase Bdatos
    ----------------
    - Maneja la conexión con una base de datos SQLite local.
    - Permite crear tablas, insertar datos desde un DataFrame y realizar consultas.
    """

    def __init__(self, nombre_bd: str = "agricultura.db"):
        self.nombre_bd = nombre_bd
        self.conexion = None

    # ==================================
    # 1. Conectar y cerrar la base de datos
    # ==================================
    def conectar(self):
        """Crea la conexión con la base de datos (se crea si no existe)."""
        self.conexion = sqlite3.connect(self.nombre_bd)
        print(f"✅ Conectado a la base de datos: {self.nombre_bd}")

    def cerrar(self):
        """Cierra la conexión con la base de datos."""
        if self.conexion:
            self.conexion.close()
            print("🔒 Conexión cerrada correctamente.")

    # ==================================
    # 2. Crear tabla desde DataFrame
    # ==================================
    def crear_tabla_desde_df(self, df: pd.DataFrame, nombre_tabla: str = "agricultura"):
        """
        Crea una tabla automáticamente basada en las columnas del DataFrame.
        Si ya existe, la reemplaza.
        """
        if self.conexion is None:
            raise ConnectionError("Primero debes conectar a la base de datos con conectar().")

        df.to_sql(nombre_tabla, self.conexion, if_exists="replace", index=False)
        print(f"✅ Tabla '{nombre_tabla}' creada/reemplazada correctamente con {len(df)} registros.")

    # ==================================
    # 3. Insertar registros desde DataFrame
    # ==================================
    def insertar_df(self, df: pd.DataFrame, nombre_tabla: str = "agricultura"):
        """
        Inserta los registros del DataFrame en una tabla existente.
        No reemplaza la tabla, solo añade nuevos registros.
        """
        if self.conexion is None:
            raise ConnectionError("Primero debes conectar a la base de datos con conectar().")

        df.to_sql(nombre_tabla, self.conexion, if_exists="append", index=False)
        print(f"✅ Se insertaron {len(df)} registros en la tabla '{nombre_tabla}'.")

    # ==================================
    # 4. Consultas simples
    # ==================================
    def consultar(self, query: str) -> pd.DataFrame:
        """
        Ejecuta una consulta SQL y devuelve un DataFrame con los resultados.
        """
        if self.conexion is None:
            raise ConnectionError("Primero debes conectar a la base de datos con conectar().")

        try:
            df_result = pd.read_sql_query(query, self.conexion)
            print("✅ Consulta ejecutada correctamente.")
            return df_result
        except Exception as e:
            print("❌ Error al ejecutar la consulta:", e)
            return pd.DataFrame()
