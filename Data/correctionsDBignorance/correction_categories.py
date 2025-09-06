# Importa las librerias para interactuar con la base de datos
import pymysql
import pymysql.cursors
# Libreria para corregir ortografia
import language_tool_python 
tool=language_tool_python.LanguageToolPublicAPI("es")

# Define la conexion con la base de datos
def connect():
        return pymysql.connect(host='localhost',user="root",passwd="",db="ignorancia",cursorclass=pymysql.cursors.DictCursor)
            
# Define la funcion para corregir las categorias      
def edit_spelling_categories():
    conexion=connect()
    with conexion:
        # Crea un cursor para la conexion de la base de datos
        with conexion.cursor() as cursor:
            cursor.execute("select id_categoria,descripcion from categoria")
            registers=cursor.fetchall()
            
            # Recorre cada uno de los registros de categoria
            for register in registers:
                id_category=register["id_categoria"]
                description=register["descripcion"]
                # Imprime que categoria esta siendo corregida
                print("Corrigiendo categoria", id_category)
                
                # Llama a la funcion para revisar la categoria
                matches=tool.check(description)
                edit_category=language_tool_python.utils.correct(description,matches)
                
                print(edit_category)
                
                # Actualiza la categoria corregida
                cursor.execute("update categoria set descripcion=%s where id_categoria=%s", (edit_category, id_category))
                # Guarda los cambios
                conexion.commit()
        print("Correcion completada")
        
edit_spelling_categories()