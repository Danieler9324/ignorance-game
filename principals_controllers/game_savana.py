# Importa los archivos para el funcionamiento de las funciones
from principals_controllers.game_formula1 import screen_formula1,screen_canoas
from visual.vizualitation_tables.visual_categories import *
from visual.screens_extras.clasific_table import *
from Data.recuperation.recover_categories import *
from Data.recuperation.recover_questions import *
from classes.class_gif_players_formula1 import *
from classes.class_elephant import *
from classes.class_jeep import *
# Importa las librerias de tkinter, pygame y random
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import pygame
import random 

# Define las variables para las rondas y el vector vacio para las preguntas usadas
rouns_limi=3
rouns=int(1)
used_questio=[]

# Crea una sub-pantalla (Ejecutar el juego con una resolucion de 1366 x 768)
screen_savana = tk.Toplevel()
screen_savana.resizable(1, 1)
screen_savana.attributes("-fullscreen", True)   # Pone la pantalla principal en toda la pantalla del pc
screen_savana.config(bg="Red")

selectio=()
# Crea las variables de la pregunta y respuesta y del siguiente jugador como stringVar
str_questio=StringVar()
str_answe1=StringVar()
str_answe2=StringVar()
str_answe3=StringVar()
str_answe4=StringVar()
str_nex=StringVar()
# Define la variable de la opcion correcta y las variables de las posiciones de "x" de cada jugador
correc=0
xx1=10
xx2=10
xx3=10
xx4=10
tur=1
# Se define la variable wi(win) como vacia y contin(continue) como una variable booleana
wi=""
winner_game=""
continu=True

# Se define los puntos inciales de cada jugador
clasification_dat = {"Jeep 1": 0,"Jeep 2": 0,"Jeep 3": 0, "Ignorancia": 0}

# Define la linea de meta
finish_lin=1100

# Define la funcion para el juego de canoas
def game_savana():
    
    # Esconde las pantallas de formula1 y canoas
    screen_formula1.withdraw()
    screen_canoas.withdraw()
    
    # Define la funcion para que los jugadores avancen
    def player_advanc(): 
        # Toma variables globales
        global xx1, xx2, xx3, xx4, wi, continu, clasification_dat

        # Si la respuesta del jugador es correcta entonces avanzar hasta llegar a 10
        if tur == 1:
            start_po = xx1
            # Ejecuta el sonido de avanzar de un jeep
            sound_jeeps.play()
            for _ in range(15):
            #for _ in range(20):
                start_po += 15
                #start_po +=20
                xx1 = start_po
                advance_jeep1.place(x=xx1, y=340)
                Jeep_Stand_player1.place_forget()
                screen_savana.update()
                screen_savana.after(30)
                # Suma 200 puntos a el jugador despues de que este avance
                clasification_dat["Jeep 1"] += 20
                if xx1 >= finish_lin:
                    # Esconde la posicion de todos los jugadores y de la ignorancia
                    advance_jeep1.place_forget()
                    advance_jeep2.place_forget()
                    advance_jeep3.place_forget()
                    Ignorance_Advance.place_forget()
                    # Establece la posicion del ganador en la linea de meta
                    Jeep_Stand_player1.place(x=1100,y=340)
                    wi = "Jeep 1"
                    # Avanza a la siguiente ronda
                    reset_roun()
                    break
        
        # Si la respuesta del jugador es correcta entonces avanzar hasta llegar a 10              
        elif tur == 2:
            start_po = xx2
            # Ejecuta el sonido de avanzar de un jeep
            sound_jeeps.play()
            for _ in range(15):
            #for _ in range(20):
                start_po += 15
                #start_po +=20
                xx2 = start_po 
                advance_jeep2.place(x=xx2, y=420)
                Jeep_Stand_player2.place_forget()
                screen_savana.update()
                screen_savana.after(30)
                # Suma 200 puntos a el jugador despues de que este avance
                clasification_dat["Jeep 2"] += 20
                if xx2 >= finish_lin:                 
                    # Esconde la posicion de todos los jugadores y de la ignorancia
                    advance_jeep2.place_forget()
                    advance_jeep1.place_forget()
                    advance_jeep3.place_forget()
                    Ignorance_Advance.place_forget()
                    # Establece la posicion del ganador en la linea de meta
                    Jeep_Stand_player2.place(x=1100,y=420)
                    wi = "Jeep 2"
                    # Avanza a la siguiente ronda
                    reset_roun()
                    break
        
        # Si la respuesta del jugador es correcta entonces avanzar hasta llegar a 10
        elif tur == 3:
            start_po = xx3
            # Ejecuta el sonido de avanzar de un jeep
            sound_jeeps.play()
            for _ in range(15):
            #for _ in range(20):
                start_po += 15
                #start_po +=20
                xx3 = start_po
                advance_jeep3.place(x=xx3, y=505)
                Jeep_Stand_player3.place_forget()
                screen_savana.update()
                screen_savana.after(30)
                # Suma 200 puntos a el jugador despues de que este avance
                clasification_dat["Jeep 3"] += 20
                if xx3 >= finish_lin:
                    # Esconde la posicion de todos los jugadores y de la ignorancia
                    advance_jeep3.place_forget()
                    advance_jeep1.place_forget()
                    advance_jeep2.place_forget()
                    Ignorance_Advance.place_forget()
                    # Establece la posicion del ganador en la linea de meta
                    Jeep_Stand_player3.place(x=1100,y=505)
                    wi = "Jeep 3"
                    # Avanza a la siguiente ronda
                    reset_roun()
                    break
        
        # Si continua es Falso entonces activar los botones de respuesta y poner al ganador de la ronda
        if continu==False:
            answe.config(state=NORMAL)
            answe2.config(state=NORMAL)
            answe3.config(state=NORMAL)
            answe4.config(state=NORMAL)
            messagebox.showinfo("Ganador", wi + " ha ganado la ronda!")
            # Muestra la tabla de clasificacion
            screen_clasification(clasification_dat)

    # Define la funcion para la opcion 1
    def optio1():
        # Hace el sonido al hacer click 
        sound_click.play()
        global tur, xx4, correc_answer_tex
        # Desactiva los botones
        answe.config(state=DISABLED)
        answe2.config(state=DISABLED)
        answe3.config(state=DISABLED)
        answe4.config(state=DISABLED)

        # Si la opcion es correcta entonces avanza jugador
        if correc == 1:
            player_advanc()

        # Si la opcion no es correcta entonces avanza la ignorancia
        else:
            start_positio = xx4
            for _ in range(15):
            #for _ in range(20):
                start_positio += 15
                #start_positio += 20
                xx4 = start_positio
                Ignorance_Advance.place(x=xx4, y=600)
                Ignorance_Stand.place_forget()
                screen_savana.update()
                screen_savana.after(50)
                # Le suma 200 puntos a la ignorancia
                clasification_dat["Ignorancia"] += 20
                if xx4 >= finish_lin:
                    # Esconde a todos los jugadores y a la ignorancia
                    Ignorance_Advance.place_forget()
                    advance_jeep1.place_forget()
                    advance_jeep2.place_forget()
                    advance_jeep3.place_forget()
                    # Establece a la igrnoancia en la linea de meta
                    Ignorance_Advance.place(x=1100, y=600)
                    messagebox.showinfo("Ganador", "Ignorancia")
                    reset_roun()
                    break
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_tex}")

        tur += 1
        if tur > 3:
            tur = 1
        str_nex.set(f"Jugador {tur}")
        # Avanza a la siguiente pregunta
        advance_to_next_questio()

    # Define la funcion para la opcion 2
    def optio2():
                # Hace el sonido al hacer click 
        sound_click.play()
        global tur, xx4, correc_answer_tex
        # Desactiva los botones
        answe.config(state=DISABLED)
        answe2.config(state=DISABLED)
        answe3.config(state=DISABLED)
        answe4.config(state=DISABLED)

        # Si la opcion es correcta entonces avanza jugador
        if correc == 2:
            player_advanc()

        # Si la opcion no es correcta entonces avanza la ignorancia
        else:
            start_positio = xx4
            for _ in range(15):
            #for _ in range(20):
                start_positio += 15
                #start_positio += 20
                xx4 = start_positio
                Ignorance_Advance.place(x=xx4, y=600)
                Ignorance_Stand.place_forget()
                screen_savana.update()
                screen_savana.after(50)
                # Le suma 200 puntos a la ignorancia
                clasification_dat["Ignorancia"] += 20
                if xx4 >= finish_lin:
                    # Esconde a todos los jugadores y a la ignorancia
                    Ignorance_Advance.place_forget()
                    advance_jeep1.place_forget()
                    advance_jeep2.place_forget()
                    advance_jeep3.place_forget()
                    # Establece a la igrnoancia en la linea de meta
                    Ignorance_Advance.place(x=1100, y=600)
                    messagebox.showinfo("Ganador", "Ignorancia")
                    reset_roun()
                    break
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_tex}")

        tur += 1
        if tur > 3:
            tur = 1
        str_nex.set(f"Jugador {tur}")
        # Avanza a la siguiente pregunta
        advance_to_next_questio()

    # Define la funcion para la opcion 3
    def optio3():
                # Hace el sonido al hacer click 
        sound_click.play()
        global tur, xx4, correc_answer_tex
        # Desactiva los botones
        answe.config(state=DISABLED)
        answe2.config(state=DISABLED)
        answe3.config(state=DISABLED)
        answe4.config(state=DISABLED)

        # Si la opcion es correcta entonces avanza jugador
        if correc == 3:
            player_advanc()

        # Si la opcion no es correcta entonces avanza la ignorancia
        else:
            start_positio = xx4
            for _ in range(15):
            #for _ in range(20):
                start_positio += 15
                #start_positio += 20
                xx4 = start_positio
                Ignorance_Advance.place(x=xx4, y=600)
                Ignorance_Stand.place_forget()
                screen_savana.update()
                screen_savana.after(50)
                # Le suma 200 puntos a la ignorancia
                clasification_dat["Ignorancia"] += 20
                if xx4 >= finish_lin:
                    # Esconde a todos los jugadores y a la ignorancia
                    Ignorance_Advance.place_forget()
                    advance_jeep1.place_forget()
                    advance_jeep2.place_forget()
                    advance_jeep3.place_forget()
                    # Establece a la igrnoancia en la linea de meta
                    Ignorance_Advance.place(x=1100, y=600)
                    messagebox.showinfo("Ganador", "Ignorancia")
                    reset_roun()
                    break
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_tex}")

        tur += 1
        if tur > 3:
            tur = 1
        str_nex.set(f"Jugador {tur}")
        # Avanza a la siguiente pregunta
        advance_to_next_questio()

    # Define la funcion para la opcion 4
    def optio4():
                # Hace el sonido al hacer click 
        sound_click.play()
        global tur, xx4, correc_answer_tex
        # Desactiva los botones
        answe.config(state=DISABLED)
        answe2.config(state=DISABLED)
        answe3.config(state=DISABLED)
        answe4.config(state=DISABLED)

        # Si la opcion es correcta entonces avanza jugador
        if correc == 4:
            player_advanc()

        # Si la opcion no es correcta entonces avanza la ignorancia
        else:
            start_positio = xx4
            for _ in range(15):
            #for _ in range(20):
                start_positio += 15
                #start_positio += 20
                xx4 = start_positio
                Ignorance_Advance.place(x=xx4, y=600)
                Ignorance_Stand.place_forget()
                screen_savana.update()
                screen_savana.after(50)
                # Le suma 200 puntos a la ignorancia
                clasification_dat["Ignorancia"] += 20
                if xx4 >= finish_lin:
                    # Esconde a todos los jugadores y a la ignorancia
                    Ignorance_Advance.place_forget()
                    advance_jeep1.place_forget()
                    advance_jeep2.place_forget()
                    advance_jeep3.place_forget()
                    # Establece a la igrnoancia en la linea de meta
                    Ignorance_Advance.place(x=1100, y=600)
                    messagebox.showinfo("Ganador", "Ignorancia")
                    reset_roun()
                    break
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_tex}")

        tur += 1
        if tur > 3:
            tur = 1
        str_nex.set(f"Jugador {tur}")
        # Avanza a la siguiente pregunta
        advance_to_next_questio()
    
    # Define la funcion para  ir a la siguiente ronda
    def reset_roun():
        # Detiene el sonido de los jeeps
        sound_jeeps.stop()
        # Toma varianles globales
        global xx1, xx2, xx3, xx4, correc, tur, used_questio, rouns, rouns_limi, continu, wi, winner_game,button_end_game

        # Reinicia las posiciones de x de los jugadores
        xx1 = 10
        xx2 = 10
        xx3 = 10
        xx4 = 10
        
        # Reinicia la posicion de los jugadores
        Ignorance_Advance.place(x=xx4, y=600)
        advance_jeep1.place(x=xx1, y=340)
        advance_jeep2.place(x=xx2, y=420)
        advance_jeep3.place(x=xx3, y=505)

        Ignorance_Stand.place(x=xx4, y=600)        
        Jeep_Stand_player1.place(x=xx1, y=340)
        Jeep_Stand_player2.place(x=xx2, y=420)
        Jeep_Stand_player3.place(x=xx3, y=505)

        # Reinicia el turno y el ganador
        tur = 0
        wi = ""
        # Habilita los botones
        answe.config(state=NORMAL)
        answe2.config(state=NORMAL)
        answe3.config(state=NORMAL)
        answe4.config(state=NORMAL)
        str_nex.set(f"Jugador {tur}")

        # Si la variable rounds es igual o mayor a rounds limit entonces calcular quien fue el que tuvo mas puntos
        if rouns >= rouns_limi:
            max_score = max(clasification_dat.values())
            winners = [key for key, value in clasification_dat.items() if value == max_score]
            
            if len(winners) == 1:
                winner_game = winners[0]
                # Si gano la ignorancia mostrar el gif de game over y el sonido de derrota
                if winner_game == "Ignorancia":
                    sound_jeeps.stop()
                    sound_end_game.play()
                    
                    defeat = GIFElephant(screen_savana, "visual/gifs/animations_win/Ignorance_Won.gif")
                    defeat.place(x=400,y=200)
                    
                    button_end_game_image = PhotoImage(file=r"visual/images/buttons_images/buttons_savana/End_Button.png")
                    button_end_game = Button(screen_savana,image=button_end_game_image,command=end_game_button_action,bg="Black")
                    button_end_game.place(x=680, y=420)
                
                # Si gano un Jugador entonces poner el sonido de vitoriay mostrar el gif de cual jugador gano
                else:
                    
                    if winner_game == "Jeep 1":
                        sound_win.play()
                        win_jeep1 = GIFElephant(screen_savana, "visual/gifs/animations_win/1_Player_won.gif")
                        win_jeep1.place(x=400,y=200)
                        
                        button_end_game_image = PhotoImage(file=r"visual/images/buttons_images/buttons_savana/End_Button.png")
                        button_end_game = Button(screen_savana,image=button_end_game_image,command=end_game_button_action,bg="Black")
                        button_end_game.place(x=680, y=420)
                        screen_clasification(clasification_dat)
                        win_jeep1.play()
                        
                        sound_jeeps.stop()
                        
                    if winner_game == "Jeep 2":
                        sound_win.play()
                        
                        win_jeep2 = GIFElephant(screen_savana, "visual/gifs/animations_win/2_Player_won.gif")
                        win_jeep2.place(x=400,y=200)
                        
                        button_end_game_image = PhotoImage(file=r"visual/images/buttons_images/buttons_savana/End_Button.png")
                        button_end_game = Button(screen_savana,image=button_end_game_image,command=end_game_button_action,bg="Black")
                        button_end_game.place(x=680, y=420)
                        screen_clasification(clasification_dat)
                        win_jeep2.play()
                        sound_jeeps.stop()
                        
                    if winner_game == "Jeep 3":
                        sound_win.play()
                        
                        win_jeep3 = GIFElephant(screen_savana, "visual/gifs/animations_win/3_Player_won.gif")
                        win_jeep3.place(x=400,y=200)

                        button_end_game_image = PhotoImage(file=r"visual/images/buttons_images/buttons_savana/End_Button.png")
                        button_end_game = Button(screen_savana,image=button_end_game_image,command=end_game_button_action,bg="Black")
                        button_end_game.place(x=680, y=420)
                        screen_clasification(clasification_dat)
                        win_jeep3.play()
                        
                        sound_jeeps.stop()
            # Si fue empate entonces mostrar el mensaje de quien y quien fue el empate
            else:
                messagebox.showinfo("Empate", f"¡Hay un empate entre los siguientes jugadores: {', '.join(winners)}!")
            screen_clasification(clasification_dat)
        # Si no es ninguno de los anteriores entonces mostrar una nueva ronda
        else:
            rouns += 1
            messagebox.showinfo("Nueva ronda", f"Inicia la ronda {rouns}")
            select_questio()
            
    # Funcion para el boton de terminar partida, que aparece al finalizar un juego
    def end_game_button_action():
        global button_end_game
        if button_end_game:
            # Despues de que el boton es presionado se destruye
            button_end_game.destroy()
        # Se destruye la pantalla de canoas
        screen_canoas.destroy()

    # Define la funcion para avanzar a la siguiente pregunta
    def advance_to_next_questio():
        # Toma variables globales
        global rouns, continu

        # Usa un ciclo for para verificar que la pregunta no a sido usada
        if len([questio for questio in selectio if questio[0] not in used_questio]) > 0:
            select_questio()
        # Verifica que rounds sea menor que 1, y si lo es entonces mostrar mensaje
        else:
            rouns += 1
            if rouns < 1:
                messagebox.showinfo("Comienza la ronda"+ rouns + 1)
                used_questio.clear()
                select_questio()
            # Si no, mostrar que no hay preguntas disponibles y quitar las opciones
            else:
                str_questio.set("Ya no hay preguntas disponibles")
                str_answe1.set("")
                str_answe2.set("")
                str_answe3.set("")
                str_answe4.set("")

                # Desactivar los botones
                for btn in [answe, answe2, answe3, answe4]:
                    if btn.winfo_exists():
                        btn.config(state=NORMAL)
    
    # Define la funcion para seleccionas las pregutnas
    def select_questio():
        # Toma variables globales
        global correc, correc_answer_tex
        # Crea un ciclo for parara revisar las preguntas que no han sido usadas
        unused_questio = [questio for questio in selectio if questio[0] not in used_questio]

        if unused_questio:
            # Elige una pregunta aleatoria de las que no han sido usadas
            question_dat = random.choice(unused_questio)
            used_questio.append(question_dat[0])
            str_questio.set(question_dat[2])
            str_answe1.set(question_dat[3])
            str_answe2.set(question_dat[4])
            str_answe3.set(question_dat[5])
            str_answe4.set(question_dat[6])
            correc = question_dat[7]
            # Variable para mostrar la respuesta correcta
            correc_answer_tex = question_dat[2 + correc]

            answe.config(state=NORMAL)
            answe2.config(state=NORMAL)
            answe3.config(state=NORMAL)
            answe4.config(state=NORMAL)
        # Si no, mostrar  que ya no hay preguntas disponibles
        else:
            str_questio.set("Ya no hay preguntas disponibles")
            str_answe1.set("")
            str_answe2.set("")
            str_answe3.set("")
            str_answe4.set("")
            
            for btn in [answe, answe2, answe3, answe4]:
                if btn.winfo_exists():
                    btn.config(state=NORMAL)

    # Define la funcion answ
    def asnwe(even):
        global selectio
        # Obtiene el valor de la categoria
        ca = even.widget.get()
        # Reemplaza los espacios por guiones bajos
        ca=str(ca).replace("_"," ")
        selectio = recover_questions(ca)
        select_questio()
    
    # Define la funcion de seleccionar todas las preguntnas
    def select_all_questio():
        # Hace el sonido de hacer click
        sound_click.play()
        global selectio
        # Llama a la funcion para recuperar todas las preguntas
        all_question = recover_questions("all")
        selectio = all_question
        select_questio()

    # Define la funcion para editar las categorias
    def edit_categorie():
        sound_click.play()
        screen_categories()
    
    # Define la funcion para terminar el juego
    def end_gam():
        # Destruye la pantalla de savana
        screen_savana.destroy()
    
    # Recupera las categorias
    l_categorie = recover_categories()
    cas = []
    for ca in l_categorie:
        ca2=str(ca[0])
        cas.append(ca2)
    
    # Inicia el mixer de pygame
    pygame.init()
    pygame.mixer.init()
    
    # Define los efectos de sonido
    sound_end_game = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/Fin_del_juego_savana.mp3")
    sound_end_game.set_volume(1.0)
    
    sound_win = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/jugador_gano_savana.mp3")
    sound_win.set_volume(1.0)
    
    sound_jeeps = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/Para_Carros_de_Savana.mp3")
    sound_jeeps.set_volume(1.0)
    
    # Define el boton de terminar partida cuando la ignorancia o un jugador gana
    button_end_game_img = PhotoImage(file=r"visual/images/buttons_images/buttons_savana/End_Button.png")
    button_end_game = Button(screen_savana, image=button_end_game_img, command=end_gam, background="Yellow")
    button_end_game.place(x=400,y=250)
    
    # Define el fondo y pista de la savana
    image_savana = Image.open("visual/images/tracks_images/savana.png").convert("RGBA")
    bg_savana_color = Image.new("RGBA", image_savana.size, screen_savana["bg"])  
    image_savana_with_bg = Image.alpha_composite(bg_savana_color, image_savana)  

    image_tk = ImageTk.PhotoImage(image_savana_with_bg)
    # Establece la posicion de la pista de savana
    label_image_savana = tk.Label(screen_savana, image=image_tk, bg="#ffbd4a")
    label_image_savana.place(x=1,y=1)
    
    # Define la etiqueta de categorias como una images
    image_etiquet_categories=PhotoImage(file=r"visual/images/buttons_images/buttons_savana/Category.png")
    etiquet_categories = Label(screen_savana, image=image_etiquet_categories ,bg="#ffbd4a")
    etiquet_categories.place(x=13, y=38)

    # Define el combobox de la categorias con un tamaño de 12 y fuente Arial
    categoris = ttk.Combobox(screen_savana, font="Helvetica 18 bold")
    categoris["values"]=cas
    categoris["font"]=("Arial", 18)
    screen_savana.option_add("*TCombobox*Listbox.font", ("Arial", 12))
    categoris.place(x=145, y=40)
    categoris.bind("<<ComboboxSelected>>", asnwe)
    
    # Define el boton del catalogo
    image_catalog = PhotoImage(file=r"visual/images/buttons_images/button_catalog.png")
    button_catalo=Button(screen_savana, image=image_catalog, command=edit_categorie,bg="#ffbd4a")
    button_catalo.place(x=1000, y=30)

    # Define la etiqueta que dice cual es el jugador en turno
    str_nex.set("Jugador 1")
    next_playe = Label (screen_savana,bg="#ffbd4a",textvariable=str_nex,font="Helvetica 18 bold")
    next_playe.place(x=800,y=40)

    # Define la etiqueta de la pregunta
    image_question_etiquet= PhotoImage(file=r"visual/images/buttons_images/buttons_savana/Question.png")
    question_etique = Label(screen_savana, bg="#ffbd4a", image=image_question_etiquet)
    question_etique.place(x=13, y=90)

    # Define lo que va a ir adentro de la stringVar de la pregunta
    str_questio.set("")
    questio = Label(screen_savana, textvariable=str_questio, font="Helvetica 18 bold", bg="Lavender", width=60, wraplength=900, justify=LEFT)
    questio.place(x=145, y=90)

    # Define la imagen del boton de todas
    image_button_all_questio = PhotoImage(file=r"visual/images/buttons_images/buttons_savana/All_Button.png")
    button_all_questio = Button(screen_savana, image=image_button_all_questio, command=select_all_questio, bg="#ffbd4a")
    button_all_questio.place(x=500, y=40)

    # Define los botones de respuesta asi como su longitud y su color
    str_answe1.set("")
    answe = Button(screen_savana, textvariable=str_answe1, command=optio1, font="Helvetica 14 bold", bg="#ffbd4a", width=70,justify=LEFT)
    answe.place(x=200, y=150)
    
    str_answe2.set("")
    answe2 = Button(screen_savana, textvariable=str_answe2, command=optio2, font="Helvetica 14 bold", bg="#ffbd4a", width=70,justify=LEFT)
    answe2.place(x=200, y=192)
    
    str_answe3.set("")
    answe3 = Button(screen_savana, textvariable=str_answe3, command=optio3, font="Helvetica 14 bold", bg="#ffbd4a", width=70,justify=LEFT)
    answe3.place(x=200, y=235)

    str_answe4.set("")
    answe4 = Button(screen_savana, textvariable=str_answe4, command=optio4, font="Helvetica 14 bold", bg="#ffbd4a", width=70,justify=LEFT)
    answe4.place(x=200, y=280)

    # Define el boton de terminar partida
    button_le = tk.Button(screen_savana, text="Terminar Partida", command=end_gam, font="Helvetica 9 bold", width=200, bg="#9c9c9c",fg="Black")
    button_le.place(x=1, y=1) 
    
    # Define las animacion de cada jugador ya sea cuando esta parado y avanzando
    advance_jeep1=GIFJeep(screen_savana, "visual/images/players_images/Jeeps/Jeep_Advance_player_1.gif")
    advance_jeep1.config(bg="#68480e")
    advance_jeep1.play()
    
    advance_jeep2=GIFJeep(screen_savana,"visual/images/players_images/Jeeps/Jeep_Advance_player_2.gif")
    advance_jeep2.config(bg="#68480e")
    advance_jeep2.play()
    
    advance_jeep3=GIFJeep(screen_savana, "visual/images/players_images/Jeeps/Jeep_Advance_player_3.gif")
    advance_jeep3.config(bg="#68480e")
    advance_jeep3.play()
    
    Jeep_Stand_player1 = GIFJeep(screen_savana, "visual/images/players_images/Jeeps/Jeep_Stand_player_1.gif")
    Jeep_Stand_player1.config(bg="#68480e")
    Jeep_Stand_player1.place(x=10, y=340)

    Jeep_Stand_player2 = GIFJeep(screen_savana, "visual/images/players_images/Jeeps/Jeep_Stand_player_2.gif")
    Jeep_Stand_player2.config(bg="#68480e")
    Jeep_Stand_player2.place(x=10, y=420)

    Jeep_Stand_player3 = GIFJeep(screen_savana, "visual/images/players_images/Jeeps/Jeep_Stand_player_3.gif")
    Jeep_Stand_player3.config(bg="#68480e")
    Jeep_Stand_player3.place(x=10, y=505)

    # Define la posicion de la ignorancia, cuando esta parado o avanzando
    Ignorance_Stand = GIFElephant(screen_savana, "visual/images/players_images/Jeeps/Ignorance_Stand.gif")
    Ignorance_Stand.config(bg="#68480e")
    Ignorance_Stand.place(x=10,y=600)
    
    Ignorance_Advance = GIFElephant(screen_savana, "visual/images/players_images/Jeeps/Ignorance_Advance.gif")
    Ignorance_Advance.config(bg="#68480e")
    Ignorance_Advance.play()
    
    # Define el boton de clasificacion
    image_button_clasificatio = PhotoImage(file=r"visual/images/buttons_images/buttons_savana/Score_Button.png")
    button_clasificatio = tk.Button(screen_savana, image=image_button_clasificatio, command=lambda:screen_clasification(clasification_dat),bg="#ffbd4a")
    button_clasificatio.place(x=1100, y=40)

    # Muestra la pantalla
    screen_savana.mainloop()