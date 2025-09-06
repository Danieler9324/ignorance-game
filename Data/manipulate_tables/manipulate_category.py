# Importa la libreria pymysql para  interactuar con la base de datos
import pymysql

# Define la tabla de categorias
def categories_table():
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    cursor.execute("select id_categoria,descripcion from categoria")
    # Selecciona todos los registros de la tabla categoria
    categories=cursor.fetchall()
    # Cierra la conexion con la base de datos
    conn.close
    return categories

# Define la funcion para agregar una categoria 
def insert_category(description):
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Agrega la categoria solicitada
    cursor.execute("insert into categoria(descripcion) values(%s)", (description))
    # Guarda los cambios
    conn.commit()
    conn.close()

# Define la funcion para eliminar categorias
def delete_categories(ab):
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Eliminar la categoria seleccionada
    cursor.execute("delete from categoria where id_categoria=%s", (ab))
    # Guarda los cambios
    conn.commit()
    conn.close()

# Define la funcion para seleccionar la categoria
def select_categories(ab):
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Selecciona la categoria solicitada
    cursor.execute("SELECT id_categoria, descripcion FROM categoria WHERE id_categoria=%s", (ab,))
    # Selecciona un registro de la tabla categoria
    dato=cursor.fetchone()
    return dato

# Define la funcion para actualizar la categoria
def update_categories(ab,description):
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Actualiza la categoria seleccionada
    cursor.execute("update categoria set descripcion=%s where id_categoria=%s",(description,ab))
    # Guarda los cambios
    conn.commit()
    conn.close()