# Importa las librerias para interactuar con la base de datos
import pymysql
import pymysql.cursors
# Importa la libreria para corregir faltas de ortografia
import language_tool_python 
tool=language_tool_python.LanguageToolPublicAPI("es")

# Define la conexion con la base de datos
def connect():
        return pymysql.connect(host='localhost',user="root",passwd="",db="ignorancia",cursorclass=pymysql.cursors.DictCursor)

# Define la funcion para corregir ortografia
def edit_spelling_questions():
    conexion=connect()
    with conexion:
        # Crea un cursor para la conexion de la base de datos
        with conexion.cursor() as cursor:
            cursor.execute("select id_pregunta,pregunta,op1,op2,op3,op4 from preguntas")
            registers=cursor.fetchall()
            
            # Recorre cada uno de los registros de pregunta
            for register in registers:
                id_question=register["id_pregunta"]
                question=register["pregunta"]
                op1=register["op1"]
                op2=register["op2"]
                op3=register["op3"]
                op4=register["op4"]
                print("Corrigiendo pregunta", id_question)
            
                # Llama a la herramienta para revisar la ortografia para la pregunta
                matches=tool.check(question)
                edit_question=language_tool_python.utils.correct(question,matches)
                
                # Llama a la herramienta para revisar la ortografia para la opcion 1
                matches=tool.check(op1)
                edit_op1=language_tool_python.utils.correct(op1,matches)
                
                # Llama a la herramienta para revisar la ortografia para la opcion 2
                matches=tool.check(op2)
                edit_op2=language_tool_python.utils.correct(op2,matches)
                
                # Llama a la herramienta para revisar la ortografia para la opcion 3
                matches=tool.check(op3)
                edit_op3=language_tool_python.utils.correct(op3,matches)
                
                # Llama a la herramienta para revisar la ortografia para la opcion 4
                matches=tool.check(op4)
                edit_op4=language_tool_python.utils.correct(op4,matches)
                print(edit_question)
                
                # Actualiza la pregunta corregida
                cursor.execute("update preguntas set pregunta=%s, op1=%s, op2=%s, op3=%s, op4=%s where id_pregunta=%s",(edit_question,edit_op1,edit_op2,edit_op3,edit_op4,id_question))
                # Guarda los cambios
                conexion.commit()
        print("Correcion completada")
        
edit_spelling_questions()