# Importan losarchivos necesarios para el funcionamiento
from Data.manipulate_tables.manipulate_question import *
from Data.recuperation.recover_questions import *
from Data.conection import *
# Importa las librerias de tkinter y pygame
from tkinter import ttk
from tkinter import *
import pygame

# inicia el mixer de pygame
pygame.init()
pygame.mixer.init()

# Define el efecto de sonido de click
sound_click = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/Sonido_al_hacer_click.mp3")
sound_click.set_volume(1.0)

# Define la variable que contiene la pantalla de la tabla de preguntas
def screen_questions(data):
    id=data[0]
    # Define la pantalla de preguntas encima de la de categorias
    screen_questions=Toplevel()
    screen_questions.resizable(1,1)
    screen_questions.geometry("1250x550")
    screen_questions.config(background="#9da1aa")
    screen_questions.title("Catalogo de Preguntas")
    # Define la cateogria, pregunta, opciones y la respuesta como stringVar
    str_category=StringVar()
    str_question=StringVar()
    str_op1=StringVar()
    str_op2=StringVar()
    str_op3=StringVar()
    str_op4=StringVar()
    str_answ=StringVar()
    
    # Crea un marco para la tabla de preguntas
    frame_questions=Frame(screen_questions)
    frame_questions.pack()
    frame_questions.place(x=20,y=250)
    scroll=ttk.Scrollbar(frame_questions,orient=VERTICAL)
    scroll.pack(side=RIGHT,fill=Y)
    
    # Crea los encabezados para la tabla de preguntas
    question_table=ttk.Treeview(frame_questions,columns=("pregunta","op1","op2","op3","op4","correcto"),yscrollcommand=scroll.set)
    
    question_table.column("#0",width=50)
    question_table.column("pregunta",width=500)
    question_table.column("op1",width=150)
    question_table.column("op2",width=150)
    question_table.column("op3",width=150)
    question_table.column("op4",width=150)
    question_table.column("correcto",width=50)
    question_table.pack()
    
    question_table.heading("#0")
    question_table.heading("pregunta",text="Preguntas")
    question_table.heading("op1",text="Opc.1")
    question_table.heading("op2",text="Opc.2")
    question_table.heading("op3",text="Opc.3")
    question_table.heading("op4",text="Opc.4")
    question_table.heading("correcto",text="Correcto")
    question_table.pack()
    
    scroll.config(command=question_table.yview)
    
    # Recupera las preguntas de la base de datos
    def recuperate_questions(ide):
        for record in question_table.get_children():
            question_table.delete(record)
        questions=questions_table(ide)
        for question in questions:
            question_table.insert(parent="",index="end",iid=question[0],text=str(question[0]),values=(str(question[1]).replace(" ", "_"),str(question[2]).replace(" ", "_"),str(question[3]).replace(" ", "_"),str(question[4]).replace(" ", "_"),str(question[5]).replace(" ", "_"),str(question[6]).replace(" ", "_")))
    
    # Funcion para agregar una pregunta
    def add_question():
        data=(str_question.get(),str_op1.get(),str_op2.get(),str_op3.get(),str_op4.get(),str_answ.get())
        insert_questions(data,id)
        recuperate_questions(id)   
    
    # Funcion para eliminar una pregunta
    def delete_question():
        ab=question_table.selection()[0]
        delete_questions(ab)
        recuperate_questions(id)
    
    # Funcion para modificar una pregunta
    def update_question():
        ab=question_table.selection()[0]
        data=(str_question.get(),str_op1.get(),str_op2.get(),str_op3.get(),str_op4.get(),str_answ.get())
        update_questions(ab,data)
        recuperate_questions(id)
    
    # Funcion para seleccionar una pregunta
    def select_question():
        ab=question_table.selection()[0]
        data=select_questions(ab)
        str_question.set(data[1])
        str_op1.set(data[2])
        str_op2.set(data[3])
        str_op3.set(data[4])
        str_op4.set(data[5])
        str_answ.set(data[6])
    
    recuperate_questions(id)
    str_category.set(data[0])
    str_question.set("")
    str_op1.set("")
    str_op2.set("")
    str_op3.set("")
    str_op4.set("")
    str_answ.set("")
    
    # Define las etiquetas y entradas de informacion de los parametros de la pregunta
    etiquet=Label(screen_questions,text="Categoria",bg="#9da1aa", font="Helvetica 14 bold").place(x=20,y=20)
    category=Entry(screen_questions,textvariable=str_category,font="Helvetica 14 bold", bg="Lavender",width=50,state=DISABLED).place(x=120,y=20)
    
    etiquet2=Label(screen_questions,text="question",bg="#9da1aa", font="Helvetica 14 bold").place(x=20,y=60)
    question=Entry(screen_questions,textvariable=str_question,font="Helvetica 14 bold", bg="Lavender",width=80,).place(x=120,y=60)
    
    etiquet3=Label(screen_questions,text="Opcion 1",bg="#9da1aa", font="Helvetica 14 bold").place(x=20,y=90)
    opc1=Entry(screen_questions,textvariable=str_op1,font="Helvetica 14 bold", bg="Lavender",width=30).place(x=120,y=90)
    
    etiquet4=Label(screen_questions,text="Opcion 2",bg="#9da1aa", font="Helvetica 14 bold").place(x=550,y=90)
    opc2=Entry(screen_questions,textvariable=str_op2,font="Helvetica 14 bold", bg="Lavender",width=30).place(x=670,y=90)
    
    etiqueta5=Label(screen_questions,text="Opcion 3",bg="#9da1aa", font="Helvetica 14 bold").place(x=20,y=120)
    opc3=Entry(screen_questions,textvariable=str_op3,font="Helvetica 14 bold", bg="Lavender",width=30).place(x=120,y=120)
    
    etiquet6=Label(screen_questions,text="Opcion 4",bg="#9da1aa", font="Helvetica 14 bold").place(x=550,y=120)
    opc4=Entry(screen_questions,textvariable=str_op4,font="Helvetica 14 bold", bg="Lavender",width=30).place(x=670,y=120)
    
    etiquet7=Label(screen_questions,text="Correcto",bg="#9da1aa", font="Helvetica 14 bold").place(x=20,y=150)
    answer=Entry(screen_questions,textvariable=str_answ,font="Helvetica 14 bold", bg="Lavender",width=30).place(x=120,y=150)
    
    # Define los botones para agregar,modificar,eliminar y seleccionar de la pantalla de preguntas
    button_add=Button(screen_questions,text="Agregar Preguntas",command=add_question,fg="White",bg="Black",font="Arial 12").place(x=200,y=200)
    button_update=Button(screen_questions,text="Modifica Preguntas",command=update_question,fg="White",bg="Black",font="Arial 12").place(x=400,y=200)
    button_delete=Button(screen_questions,text="Eliminar Preguntas",command=delete_question,fg="White",bg="Black",font="Arial 12").place(x=600,y=200)
    button_select=Button(screen_questions,text="Seleccion Preguntas",command=select_question,fg="White",bg="Black",font="Arial 12").place(x=800,y=200)
    
    screen_questions.mainloop()