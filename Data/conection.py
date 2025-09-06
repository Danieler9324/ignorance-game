# Importa la libreria de pymysql que interactua con la base de datos
import pymysql

# Define la funcion de recupera base de datos
def recover_bd():
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    
    # Toma todos los registros de la tabla de categoria
    cursor.execute("select id_categoria from categoria")
    # Toma todos los registros
    categories=cursor.fetchall()
    print(categories)
    
    # Toma todos los registros de la tabla de preguntas
    cursor.execute("select id_pregunta,id_categoria,pregunta,op1,op2,op3,op4,correcto from preguntas")
    # Toma todos los registros
    questions=cursor.fetchall()
    print(questions)
    
    # Cierra la conexion con la base de datos
    conn.close()
    
recover_bd()