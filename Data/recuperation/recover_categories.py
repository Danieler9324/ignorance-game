# Importa la libreria pymysql para interactuar con la base de datos
import pymysql

# Define la funcion para recuperar categorias
def recover_categories():
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Agarra todos los registros de la tabla categoria
    cursor.execute("select descripcion from categoria")
    # Toma todos los registros
    categories=cursor.fetchall()
    # Cierra la conexion
    conn.close()
    return categories