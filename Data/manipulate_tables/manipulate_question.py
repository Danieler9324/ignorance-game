# Importa la libreria de pymysql para la conexion con la base de datos
import pymysql

# Define la funcion de la tabla de preguntas
def questions_table(id):
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Selecciona todos los registros de la tabla de preguntas
    cursor.execute("select id_pregunta,pregunta,op1,op2,op3,op4,correcto,id_categoria from preguntas where id_categoria=%s",(id,))
    questions=cursor.fetchall()
    conn.close()
    return questions
    
def select_questions(ab):
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Selecciona 1 de los registros de la tabla preguntas
    cursor.execute("select id_pregunta,pregunta,op1,op2,op3,op4,correcto,id_categoria from preguntas where id_pregunta=%s", (ab,))
    # Toma el registro seleccionado
    dato=cursor.fetchone()
    return dato

def update_questions(ab,datos):
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Actualiza la pregunta solicitada
    cursor.execute("update preguntas set pregunta=%s,op1=%s,op2=%s,op3=%s,op4=%s,correcto=%s where id_pregunta=%s",(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],ab))
    # Guarda los cambios
    conn.commit()
    conn.close()
    
def delete_questions(ab):
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Elimina la pregunta solicitada
    cursor.execute("delete from preguntas where id_pregunta=%s", (ab,))
    # Guarda los cambios
    conn.commit()
    conn.close()

def insert_questions(datos,id):
    # Hace la conexion con la base de datos
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="ignorancia")
    cursor=conn.cursor()
    # Agrega la pregunta solicitada
    cursor.execute("insert into preguntas (pregunta,op1,op2,op3,op4,correcto,id_categoria) values (%s,%s,%s,%s,%s,%s,%s)",(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],id))
    # Guarda los cambios
    conn.commit()
    conn.close()