# importa los archivos para  el funcionamiento de la pantalla de categorias
from visual.vizualitation_tables.visual_questions import *
from Data.manipulate_tables.manipulate_question import *
from Data.manipulate_tables.manipulate_category import *
# Importa la libreria de tkinter y pygame
from tkinter import ttk
from tkinter import *
import pygame

# Inicia el mixer de pygame
pygame.init()
pygame.mixer.init()

# Define el efecto de sonido al hacer click
sound_click = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/Sonido_al_hacer_click.mp3")
sound_click.set_volume(1.0)

# Define la funcion para la pantalla de categorias
def screen_categories():
    # Define la pantalla de categorias como una pantalla flotante
    screen_categories=Toplevel()
    screen_categories.resizable(1,1)
    screen_categories.geometry("750x350")
    screen_categories.config(background="#9da1aa")
    screen_categories.title("Catalogo Categorias")
    # Define la variable de categoria como una stringVar
    str_category=StringVar()
    data=()
    
    # Crea un marco para las categorias
    frame=Frame(screen_categories)
    frame.pack()
    frame.place(x=20, y=100)
    scroll=ttk.Scrollbar(frame,orient=VERTICAL)
    scroll.pack(side=RIGHT,fill=Y)
    
    # Crea el encabezado para la tabla de categorias
    category_table=ttk.Treeview(frame,columns=("col1"), yscrollcommand=scroll.set)
    category_table.column("#0",width=155)
    category_table.column("col1",width=500)
    category_table.heading("#0",text="Id_categora")
    category_table.heading("col1",text="Descripcion")
    category_table.pack()
    
    scroll.config(command=category_table.yview)
    
    # Recupera la base de datos
    def recover_db():
        for record in category_table.get_children():
            category_table.delete(record)
        categs=categories_table()
        for categ in categs:
            category_table.insert(parent="",index="end",iid=categ[0],text=str(categ[0]), values=(str(categ[1]).replace(" ", "_")))
    
    # Funcion para agregar una categoria
    def add_category():
        sound_click.play()
        insert_category(str_category.get())
        recover_db()
    
    # Funcion para eliminar una categoria
    def delete_category():
        sound_click.play()
        ab=category_table.selection()[0]
        delete_categories(ab)
        recover_db()
        button_update.config(state=DISABLED)
        button_delete.config(state=DISABLED)

    # Funcion para modificar una categoria
    def update_category():
        sound_click.play()
        ab=category_table.selection()[0]
        update_categories(ab,str_category.get())
        screen_categories.update()
        recover_db()
        button_update.config(state=DISABLED)
        button_delete.config(state=DISABLED)

    # Funcion para seleccionar una categoria
    def select_category():
        sound_click.play()
        global datos
        ab=category_table.selection()[0]
        datos=select_categories(ab)
        str_category.set(datos[1])
        button_update.config(state=NORMAL)
        button_delete.config(state=NORMAL)

    recover_db()
    # Define la etiqueta de Categoria
    etiquet=Label(screen_categories,text="Categoria",bg="#9da1aa", font="Helvetica 14 bold")
    etiquet.place(x=20,y=20)
    
    # Funcion para editar las preguntas
    def edit_questions():
        sound_click.play()
        global datos
        print(datos)
        screen_questions(datos)
    
    # Funcion para definiar que va a ir en la stringVar de la categoria
    str_category.set("")
    pregu=Entry(screen_categories,textvariable=str_category,font="Helvetica 14 bold",bg="Lavender",width=50)
    pregu.place(x=120,y=20)
    
    # Define la etiqueta de preguntas
    button_question=Button(screen_categories,text="Preguntas",command=edit_questions,fg="White",bg="black")
    button_question.place(x=675,y=15)
    
    # Define los botones de la pantalla de categorias
    button_add=Button(screen_categories,text="Agregar Categorias",command=add_category,fg="White",bg="black",font="Arial 12")
    button_add.place(x=1, y=50)
    
    button_update=Button(screen_categories,text="Modifica Categoria",command=update_category,fg="White",bg="black",font="Arial 12", width=20,state=DISABLED)
    button_update.place(x=150, y=50)
    
    button_delete=Button(screen_categories,text="Borrar Categoria",command=delete_category,fg="White",bg="black",font="Arial 12", width=20,state=DISABLED)
    button_delete.place(x=350,y=50)
    
    button_select=Button(screen_categories,text="Selecciona Categoria",command=select_category,fg="White",bg="black",font="Arial 12", width=20)
    button_select.place(x=550,y=50)
    
    # Muestra la pantalla
    screen_categories.mainloop()
    