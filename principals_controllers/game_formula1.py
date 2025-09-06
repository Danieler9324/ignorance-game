# Importa los archivos para el funcionamiento de las funciones
from visual.vizualitation_tables.visual_categories import *
from visual.screens_extras.clasific_table import *
from Data.recuperation.recover_categories import *
from Data.recuperation.recover_questions import *
from principals_controllers.game_canoa import screen_canoas
from classes.class_gif_players_formula1 import *
# Importa las libreriasde tkinter, pygame y random
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import random 
import pygame

# Define las variables para las rondas y el vector vacio para las preguntas usadas
rouns_limi=3
rouns=int(1)
used_questio=[]

# Crea la pantalla principal (Ejecutar el juego con una resolucion de 1366 x 768)
screen_formula1 = tk.Toplevel()
screen_formula1.resizable(1, 1)
screen_formula1.attributes("-fullscreen", True)     # Pone la sub-pantalla en todo el tamaño la pantalla del px
screen_formula1.config(bg="Red")

selectio=()
# Crea las variables de la pregunta, respuesta, siguiente juegador como un StringVar
str_questio=StringVar()
str_answe1=StringVar()
str_answe2=StringVar()
str_answe3=StringVar()
str_answe4=StringVar()
str_nex=StringVar()
# Define la variable de opcion correcta y las variables de las posiciones de x de cada jugador
correc=0
xx1=110
xx2=110
xx3=110
xx4=110
tur=1
# Se define la variable wi(win) como vacia y cotinu(continue) como variable booleana
wi=""
winner_game=""
continu=True

# Se define los puntos iniciales de cada jugador
clasification_dat = {"Green Car": 0,"Redbull Car": 0,"Purple Car": 0, "Ignorancia": 0}

# Define la linea de meta
finish_lin=1250

# Define la funcion para el juego de formula 1
def game_formula1():
    
    # Esconde la pantalla de canoas
    screen_canoas.withdraw()
    
    # Define la funcion para que los jugadores avance
    def player_advanc(): 
        # Llama a variables globales
        global xx1, xx2, xx3, xx4, wi, continu, clasification_dat

        # Si el primer jugador contesto bien entonces hacer que avance con pausas hasta llegar a 10
        if tur == 1:
            start_po = xx1
            # Iniciar el sonido cuandoo el coche avanza
            sound_cars_formula1.play()
            for _ in range(15):
            #for _ in range(20):
                start_po += 15
                #start_po +=20
                xx1 = start_po
                advance_green.place(x=xx1, y=385)
                gif_stoped_green.place_forget()
                screen_formula1.update()
                screen_formula1.after(30)
                # Sumarle 200 puntos al jugador despues de cada avance
                clasification_dat["Green Car"] += 20
                # Si el jugador llega a la linea de meta
                if xx1 >= finish_lin:
                    # Esconder a todos los jugadores y a la ignorancia
                    advance_green.place_forget()
                    advance_redbull.place_forget()
                    advance_purple.place_forget()
                    gif_shoping_cart_ignorance.place_forget()
                    # Establecer al ganador en la linea de meta
                    gif_stoped_green.place(x=1100,y=385)
                    wi = "Green Car"
                    # Ir a la siguiente ronda
                    reset_roun()
                    break
                
        # Si el jugador 2 contesto bien entonces, avanzar       
        elif tur == 2:
            start_po = xx2
            # Iniciar el sonido cuandoo el coche avanza
            sound_cars_formula1.play()
            for _ in range(15):
            #for _ in range(20):
                start_po += 15
                #start_po +=20
                xx2 = start_po 
                advance_redbull.place(x=xx2, y=470)
                gif_stoped_redbull.place_forget()
                screen_formula1.update()
                screen_formula1.after(30)
                # Sumarle 200 puntos al jugador despues de cada avance
                clasification_dat["Redbull Car"] += 20
                # Si el jugador llega a la linea de meta
                if xx2 >= finish_lin:                 
                    # Esconder a todos los jugadores y a la ignorancia
                    advance_redbull.place_forget()
                    advance_green.place_forget()
                    advance_purple.place_forget()
                    gif_shoping_cart_ignorance.place_forget()
                    # Establecer al ganador en la linea de meta
                    gif_stoped_redbull.place(x=1100,y=470)
                    wi = "Redbull Car"
                    # Ir a la siguiente ronda
                    reset_roun()
                    break
                
        # Si el jugador 3 contesto bien entonces, avanzar
        elif tur == 3:
            start_po = xx3
            # Iniciar el sonido cuandoo el coche avanza
            sound_cars_formula1.play()
            for _ in range(15):
            #for _ in range(20):
                start_po += 15
                #start_po +=20
                xx3 = start_po
                advance_purple.place(x=xx3, y=565)
                gif_stoped_purple.place_forget()
                screen_formula1.update()
                screen_formula1.after(30)
                # Sumarle 200 puntos al jugador despues de cada avance
                clasification_dat["Purple Car"] += 20
                # Si el jugador llega a la linea de meta
                if xx3 >= finish_lin:
                    # Esconder a todos los jugadores y a la ignorancia
                    advance_purple.place_forget()
                    advance_green.place_forget()
                    advance_redbull.place_forget()
                    gif_shoping_cart_ignorance.place_forget()
                    # Establecer al ganador en la linea de meta
                    gif_stoped_purple.place(x=1100,y=565)
                    wi = "Purple Car"
                    # Ir a la siguiente ronda
                    reset_roun()
                    break
        
        # Si continua es Falso entonces activar los botones de respuesta y poner  al ganador de la ronda
        if continu==False:
            answe.config(state=NORMAL)
            answe2.config(state=NORMAL)
            answe3.config(state=NORMAL)
            answe4.config(state=NORMAL)
            messagebox.showinfo("Ganador", wi + " ha ganado la ronda!")
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

        # Si la opcion no es correcta entonces avanza ignorancia
        else:
            start_positio = xx4
            for _ in range(15):
            #for _ in range(20):
                start_positio += 15
                #start_positio += 20
                xx4 = start_positio
                gif_shoping_cart_ignorance.place(x=xx4, y=655)
                shoping_cart_stoped_ignorance.place_forget()
                screen_formula1.update()
                screen_formula1.after(50)
                # Le suma 200 puntos a la ignorancia
                clasification_dat["Ignorancia"] += 20
                if xx4 >= finish_lin:
                    # Establece a la ignorancia en la linea de meta
                    gif_shoping_cart_ignorance.place(x=1100, y=655)
                    messagebox.showinfo("Ganador", "Ignorancia")
                    reset_roun()
                    break
            # Si la respuesta no es correcta mostrar el mensaje
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

        # Si la opcion no es correcta entonces avanza ignorancia
        else:
            start_positio = xx4
            for _ in range(15):
            #for _ in range(20):
                start_positio += 15
                #start_positio += 20
                xx4 = start_positio
                gif_shoping_cart_ignorance.place(x=xx4, y=655)
                shoping_cart_stoped_ignorance.place_forget()
                screen_formula1.update()
                screen_formula1.after(50)
                # Le suma 200 puntos a la ignorancia
                clasification_dat["Ignorancia"] += 20
                if xx4 >= finish_lin:
                    # Establece a la ignorancia en la linea de meta
                    gif_shoping_cart_ignorance.place(x=1100, y=655)
                    messagebox.showinfo("Ganador", "Ignorancia")
                    reset_roun()
                    break
            # Si la respuesta no es correcta mostrar el mensaje
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_tex}")

        tur += 1
        if tur > 3:
            tur = 1
        str_nex.set("Jugador " + str(tur))
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

        # Si la opcion no es correcta entonces avanza ignorancia
        else:
            start_positio = xx4
            for _ in range(15):
            #for _ in range(20):
                start_positio += 15
                #start_positio += 20
                xx4 = start_positio
                gif_shoping_cart_ignorance.place(x=xx4, y=655)
                shoping_cart_stoped_ignorance.place_forget()
                screen_formula1.update()
                screen_formula1.after(50)
                # Le suma 200 puntos a la ignorancia
                clasification_dat["Ignorancia"] += 20
                if xx4 >= finish_lin:
                    # Establece a la ignorancia en la linea de meta
                    gif_shoping_cart_ignorance.place(x=1100, y=655)
                    messagebox.showinfo("Ganador", "Ignorancia")
                    reset_roun()
                    break
            # Si la respuesta no es correcta mostrar el mensaje
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_tex}")
        tur += 1
        if tur > 3:
            tur = 1
        str_nex.set("Jugador " + str(tur))
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

        # Si la opcion no es correcta entonces avanza ignorancia
        else:
            start_positio = xx4
            for _ in range(15):
            #for _ in range(20):
                start_positio += 15
                #start_positio += 20
                xx4 = start_positio
                gif_shoping_cart_ignorance.place(x=xx4, y=655)
                shoping_cart_stoped_ignorance.place_forget()
                screen_formula1.update()
                screen_formula1.after(50)
                # Le suma 200 puntos a la ignorancia
                clasification_dat["Ignorancia"] += 20
                if xx4 >= finish_lin:
                    # Establece a la ignorancia en la linea de meta
                    gif_shoping_cart_ignorance.place(x=1100, y=655)
                    messagebox.showinfo("Ganador", "Ignorancia")
                    reset_roun()
                    break
            # Si la respuesta no es correcta mostrar el mensaje
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_tex}")
        tur += 1
        if tur > 3:
            tur = 1
        str_nex.set("Jugador " + str(tur))
        # Avanza a la siguiente pregunta
        advance_to_next_questio()

    # Define la funcion para ir a la siguiente ronda
    def reset_roun():
        # Detiene el sonido de las canoas
        sound_cars_formula1.stop()
        # Toma las variables globales
        global xx1, xx2, xx3, xx4, correc, tur, used_questio, rouns, rouns_limi, continu, wi, winner_game, button_end_game

        # Reinicia las posiciones de x de los jugadores
        xx1 = 110
        xx2 = 110
        xx3 = 110
        xx4 = 110
        
        # Reinicia el turno y el jugador
        advance_green.place(x=xx1, y=385)
        advance_redbull.place(x=xx2, y=470)
        advance_purple.place(x=xx3, y=565)

        shoping_cart_stoped_ignorance.place(x=xx4, y=655)
        gif_shoping_cart_ignorance.place(x=xx4, y=655)
        
        gif_stoped_green.place(x=xx1, y=385)
        gif_stoped_redbull.place(x=xx2, y=470)
        gif_stoped_purple.place(x=xx3, y=565)

        # Reinicia el turno y el jugador
        tur = 0
        wi = ""
        # Habilita los botones
        answe.config(state=NORMAL)
        answe2.config(state=NORMAL)
        answe3.config(state=NORMAL)
        answe4.config(state=NORMAL)
        str_nex.set(f"Jugador {tur}")

        # Si la variable  rounds es igual o mayot a rounds limit entonces calcular quien fue el que tuvo mas puntos
        if rouns >= rouns_limi:

            max_score = max(clasification_dat.values())
            winners = [key for key, value in clasification_dat.items() if value == max_score]
            
            if len(winners) == 1:
                winner_game = winners[0]
                # Si gano la ignorancia entonces mostrar el gif de game over y el sonido de derrota
                if winner_game == "Ignorancia":
                    sound_cars_formula1.stop()
                    sound_end_game.play()
                    image_defeat = PhotoImage(file=r"visual/gifs/animations_win/win_ignorance_formula1.png")
                    defeat_image = Label(screen_formula1, image=image_defeat, bg="Black")
                    defeat_image.place(x=400,y=200)
                    
                    button_end_game_image = PhotoImage(file=r"visual/images/buttons_images/buttons_formula1/End_game.png")
                    button_end_game = Button(screen_formula1,image=button_end_game_image,command=end_game_button_action,bg="Black")
                    button_end_game.place(x=680, y=420)
                    
                    screen_clasification(clasification_dat)

                # Si gano el jugador entonces poner el sonido de victoria y mostrar la images de ganar
                else:
                    sound_cars_formula1.stop()
                    sound_win.play()
                    image_win = PhotoImage(file=r"visual/gifs/animations_win/win_car_formula1.png")
                    win_image = Label (screen_formula1, image=image_win, bg="Black")
                    win_image.place(x=400, y=200)
                    
                    button_end_game_image = PhotoImage(file=r"visual/images/buttons_images/buttons_formula1/End_game.png")
                    button_end_game = Button(screen_formula1,image=button_end_game_image,command=end_game_button_action,bg="Black")
                    button_end_game.place(x=680, y=420)
                    
                    messagebox.showinfo("¡Ganador del juego!", f"El ganador del juego es: {winner_game}")
                    screen_clasification(clasification_dat)
            # Si fue un empate entonces mostrar de  quien y quien fue el empate
            else:
                messagebox.showinfo("Empate", f"¡Hay un empate entre los siguientes jugadores: {', '.join(winners)}!")
        # Si no es ninguno de los anteriores enetonces mostrar una nueva ronda
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
        screen_formula1.destroy()
        screen_canoas.destroy()
    
    # Define la funcion para avanzar a la siguiente pregunta
    def advance_to_next_questio():
        global rouns, continu

        # Ciclo for para revisar  las  preguntas usadas
        if len([questio for questio in selectio if questio[0] not in used_questio]) > 0:
            select_questio()
        # Si no hay preguntas usadas entonces comenzar rondas
        else:
            rouns += 1
            if rouns < 1:
                messagebox.showinfo("Comienza la ronda"+ rouns + 1)
                used_questio.clear()
                select_questio()
            # Si todas las preguntas estan usada entonces imprimir que ya no hay preguntas
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
    
    # Define la funcion para seleccionar preguntas
    def select_questio():
        global correc, correc_answer_tex

        # Crea un ciclo para las preguntas sin usar
        unused_questio = [questio for questio in selectio if questio[0] not in used_questio]

        # Si no se a¿han usado las preguntas entonces elegir una pregunta aleatoria
        if unused_questio:
            question_dat = random.choice(unused_questio)
            used_questio.append(question_dat[0])
            str_questio.set(question_dat[2])
            str_answe1.set(question_dat[3])
            str_answe2.set(question_dat[4])
            str_answe3.set(question_dat[5])
            str_answe4.set(question_dat[6])
            correc = question_dat[7]
            # Variable para mostrar la respuesta
            correc_answer_tex = question_dat[2 + correc]

            # Actica los botones de respuesta
            answe.config(state=NORMAL)
            answe2.config(state=NORMAL)
            answe3.config(state=NORMAL)
            answe4.config(state=NORMAL)
        
        # Si ya no hya preguntas usadas entonces mostrar que a no hya preguntas disponibles
        else:
            str_questio.set("Ya no hay preguntas disponibles")
            str_answe1.set("")
            str_answe2.set("")
            str_answe3.set("")
            str_answe4.set("")
            
            for btn in [answe, answe2, answe3, answe4]:
                if btn.winfo_exists():
                    btn.config(state=NORMAL)

    # Define la funcion de asnwe
    def asnwe(even):
        global selectio
        # Obiene el valor de la categoria
        ca = even.widget.get()
        # Reemplaza los espacios por guiones bajos
        ca=str(ca).replace("_"," ")
        selectio = recover_questions(ca)
        select_questio()
    
    # Define la funcion de seleccionar todas las preguntas
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
        # Destruye la pantalla de canoas y destruye la pantalla de formula 1
        screen_canoas.destroy()
        screen_formula1.destroy()
    
    # Recupera las categorias
    l_categorie = recover_categories()
    # Toma las categorias como un vector vacio
    cas = []
    for ca in l_categorie:
        ca2=str(ca[0])
        cas.append(ca2)
    
    # Inicia el mixer de pygame
    pygame.init()
    pygame.mixer.init()
    
    # Define los efectos de sonido con la libreria de pygame
    sound_end_game = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/Fin_del_juego_formula.mp3")
    sound_end_game.set_volume(1.0)
    
    sound_win = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/jugador_gano_formula1.mp3")
    sound_win.set_volume(1.0)
    
    sound_cars_formula1 = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/Para_Carros_de_formula1.mp3")
    sound_cars_formula1.set_volume(1.0)
    
    # Define el fondo de pantalla y la pista
    image_formula1 = Image.open("visual/images/tracks_images/formula1.png").convert("RGBA")
    bg_formula1_color = Image.new("RGBA", image_formula1.size, screen_formula1["bg"])  
    image_formula1_with_bg = Image.alpha_composite(bg_formula1_color, image_formula1)  

    image_tk = ImageTk.PhotoImage(image_formula1_with_bg)

    label_image_formula1 = tk.Label(screen_formula1, image=image_tk, bg="#9da1aa")
    label_image_formula1.place(x=1,y=1)
    
    # Define la etiqueta de  la categoria con un fondo gris
    image_etiquet_categories=PhotoImage(file=r"visual/images/buttons_images/buttons_formula1/Category.png")
    etiquet_categories = Label(screen_formula1, image=image_etiquet_categories ,bg="#9da1aa")
    etiquet_categories.place(x=13, y=38)

    # Define la combobox de las categorias, cin un formato de Arial 12
    categoris = ttk.Combobox(screen_formula1, font="Helvetica 18 bold")
    categoris["values"]=cas
    categoris["font"]=("Arial", 18)
    screen_formula1.option_add("*TCombobox*Listbox.font", ("Arial", 12))
    categoris.place(x=145, y=40)
    categoris.bind("<<ComboboxSelected>>", asnwe)
    
    # Define la imagen del catalogo con un fondo gris
    image_catalog = PhotoImage(file=r"visual/images/buttons_images/button_catalog.png")
    button_catalo=Button(screen_formula1, image=image_catalog, command=edit_categorie,bg="#9da1aa")
    button_catalo.place(x=1000, y=30)

    # Define la etiqueta de mostrar el turno del jugador
    str_nex.set("Jugador 1")
    next_playe = Label (screen_formula1,bg="#9da1aa",textvariable=str_nex,font="Helvetica 18 bold")
    next_playe.place(x=800,y=40)

    # Define la etiqueta de las preguntas, con un fondo gris
    image_question_etiquet= PhotoImage(file=r"visual/images/buttons_images/buttons_formula1/Question.png")
    question_etique = Label(screen_formula1, bg="#9da1aa", image=image_question_etiquet)
    question_etique.place(x=13, y=90)

    # Define lo que va a dentro de la stringVar de la pregunta
    str_questio.set("")
    questio = Label(screen_formula1, textvariable=str_questio, font="Helvetica 18 bold", width=60, wraplength=900, justify=LEFT)
    questio.place(x=145, y=90)

    # Define el voton de todas las preguntas y su fondo de color gris
    image_button_all_questio = PhotoImage(file=r"visual/images/buttons_images/buttons_formula1/All_Button.png")
    button_all_questio = Button(screen_formula1, image=image_button_all_questio, command=select_all_questio, bg="#9da1aa")
    button_all_questio.place(x=500, y=40)

    # Define los botones de las respuestas tanto sus comando como sus colores y longitud
    str_answe1.set("")
    answe = Button(screen_formula1, textvariable=str_answe1, command=optio1, font="Helvetica 14 bold", bg="#9da1aa", width=70,justify=LEFT)
    answe.place(x=200, y=150)
    
    str_answe2.set("")
    answe2 = Button(screen_formula1, textvariable=str_answe2, command=optio2, font="Helvetica 14 bold", bg="#9da1aa", width=70,justify=LEFT)
    answe2.place(x=200, y=192)
    
    str_answe3.set("")
    answe3 = Button(screen_formula1, textvariable=str_answe3, command=optio3, font="Helvetica 14 bold", bg="#9da1aa", width=70,justify=LEFT)
    answe3.place(x=200, y=235)

    str_answe4.set("")
    answe4 = Button(screen_formula1, textvariable=str_answe4, command=optio4, font="Helvetica 14 bold", bg="#9da1aa", width=70,justify=LEFT)
    answe4.place(x=200, y=280)

    # Define el boton de terminar partida que se encuentra en la parte superior de la pantalla de canoas
    button_le = tk.Button(screen_formula1, text="Terminar Partida", command=end_gam, font="Helvetica 9 bold", width=200, bg="#23282b",fg="White")
    button_le.place(x=1, y=1) 
    
    # Define los jugadores como GIFS tanto sus posiciones y el color de su fondo
    advance_green=GIFplayer(screen_formula1, "visual/images/players_images/formula1_cars/car_green_advance.gif")
    advance_green.config(bg="Black")
    advance_green.play()
    
    advance_redbull=GIFplayer(screen_formula1,"visual/images/players_images/formula1_cars/car_redbull_advance.gif")
    advance_redbull.config(bg="Black")
    advance_redbull.play()
    
    advance_purple=GIFplayer(screen_formula1, "visual/images/players_images/formula1_cars/car_purple_advance.gif")
    advance_purple.config(bg="Black")
    advance_purple.play()
    
    gif_stoped_green = GIFplayer(screen_formula1, "visual/images/players_images/formula1_cars/car_green_stoped.gif")
    gif_stoped_green.config(bg="Black")
    gif_stoped_green.place(x=110, y=385)

    gif_stoped_redbull = GIFplayer(screen_formula1, "visual/images/players_images/formula1_cars/car_redbull_stoped.gif")
    gif_stoped_redbull.config(bg="Black")
    gif_stoped_redbull.place(x=110, y=470)

    gif_stoped_purple = GIFplayer(screen_formula1, "visual/images/players_images/formula1_cars/car_purple_stoped.gif")
    gif_stoped_purple.config(bg="Black")
    gif_stoped_purple.place(x=110, y=565)

    # Define la imagen e animacion del carrito de compras tanto su poscicion y el color de su fondo
    image_stoped_shoping_cart = PhotoImage(file=r"visual/images/players_images/formula1_cars/shoping_cart_stoped_ignorance.png")
    shoping_cart_stoped_ignorance= Label(screen_formula1, image=image_stoped_shoping_cart)
    shoping_cart_stoped_ignorance.config(bg="Black")
    shoping_cart_stoped_ignorance.place(x=110, y=655)
    
    gif_shoping_cart_ignorance = GIFplayer(screen_formula1, "visual/images/players_images/formula1_cars/shoping_cart_advance_ignorance.gif")
    gif_shoping_cart_ignorance.config(bg="Black")
    gif_shoping_cart_ignorance.play()
    
    # Define el boton de claisificacion como image, asi tambien su posicion y el color de fondo
    image_button_clasificatio = PhotoImage(file=r"visual/images/buttons_images/buttons_formula1/Points_Buttons.png")
    button_clasificatio = tk.Button(screen_formula1, image=image_button_clasificatio, command=lambda:screen_clasification(clasification_dat),bg="#9da1aa")
    button_clasificatio.place(x=1100, y=40)

    # Ejecuta la pantalla
    screen_formula1.mainloop()