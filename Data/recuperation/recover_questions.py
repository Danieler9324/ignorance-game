# Importa la libreria de pymysql para interactuar con la base de datos
import pymysql

# recupera la tabla de preguntas con el parametro de categoria
def recover_questions(category):
    # Hace la conexcion con la base de datos
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="ignorancia")
    cursor = conn.cursor()
    # Si es presionado el boton de todas, entonces tomar cualquier pregunta
    if category == "all":
        consult = "SELECT b.id_pregunta, b.id_categoria, b.pregunta, b.op1, b.op2, b.op3, b.op4, b.correcto FROM preguntas b"
        cursor.execute(consult)
    else:
        # Selecciona la pregunta solicitada
        consult = "SELECT b.id_pregunta, b.id_categoria, b.pregunta, b.op1, b.op2, b.op3, b.op4, b.correcto FROM categoria a, preguntas b WHERE a.descripcion = %s AND b.id_categoria = a.id_categoria"
        cursor.execute(consult, (category,))
    
    # Toma todos los registros de la tabla pregunta
    questions = cursor.fetchall()
    # Cierra la conexion con la base de datos
    conn.close()
    return questions