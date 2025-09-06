# Importa los archivos para el funcionamiento de las funciones 
from visual.vizualitation_tables.visual_categories import *
from visual.screens_extras.clasific_table import *
from Data.recuperation.recover_categories import *
from Data.recuperation.recover_questions import *
from classes.class_gif_crocodile import *
from classes.class_gif_animation import *
from classes.class_gif_animation import *
from classes.class_gif_canoas import *
from classes.class_gif_track import *
# Importa las librerias de tkinter, pillow, pygame y random
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import random 
import pygame

# Define las variables para las rondas y el vector vacio para las preguntas usadas
rouns_lim=4
roun=int(1)
used_questi=[] 

# Crea la pantalla principal (Ejecutar el juego con una resolucion de 1366 x 768)
screen_canoas = tk.Tk()
screen_canoas.resizable(1, 1)
screen_canoas.attributes("-fullscreen", True)   # Pone la pantalla principal en toda la pantalla del pc
screen_canoas.config(bg="#4887e4")

selecti=()
# Crea las variables de la pregunta y respuesta y del siguiente jugador como una stringVar
str_questi=StringVar()
str_answ1=StringVar()
str_answ2=StringVar()
str_answ3=StringVar()
str_answ4=StringVar()
str_ne=StringVar()
# Define la variable de la opcion correcta y las variables de las posiciones de "x" de cada jugador
corre=0
xxx1=40
xxx2=40
xxx3=40
xxx4=40
tu=1
# Se define la variable w(win) como vacia y contin(continue) como una variable booleana
w=""
contin=True

# Se define los puntos iniciales de cada jugador
clasification_da = {"Canoa Red": 0,"Canoa Green": 0,"Canoa Purple": 0, "Crocodile": 0}

# Define la linea de meta
finish_li=1100

# Define la funcion para el juego de canoas
def game_canoas():
    
    # Define la funcion para que los jugadores avancen
    def player_advan(): 
        # Llama a las posiciones de x de cada jugador y quien gano, continua y la tabla de clasificacion
        global xxx1, xxx2, xxx3, xxx4, w, contin, clasification_da

        # Si el primer jugador contesto bien entonces hacer que avance con pausas hasta llegar a 10
        if tu == 1:
            start_p = xxx1
            # Iniciar el sonido cuando una canoa avanza
            sound_canoas.play()
            for _ in range(15):
            #for _ in range(30):
                start_p += 15
                #start_p +=30
                xxx1 = start_p
                advance_canoa_red.place(x=xxx1, y=360)
                screen_canoas.update()
                screen_canoas.after(30)
                # Sumarle 200 puntos a el jugador despues de cada avance
                clasification_da["Canoa Red"] += 20
                # Si el jugador llega a la linea de meta
                if xxx1 >= finish_li:
                    # Esconder a todos los jugadores y a la ignorancia
                    advance_canoa_red.place_forget()
                    advance_canoa_green.place_forget()
                    advance_canoa_purple.place_forget()
                    gif_crocodile.place_forget()
                    # Establecer al ganador en la linea de meta
                    advance_canoa_red.place(x=1240,y=360)
                    w = "Canoa Red"
                    # Ir a la siguiente ronda
                    reset_rou()
                    break
                
        # Si el segundo jugador contesto bien, entonces avanzar          
        elif tu == 2:
            start_p = xxx2
            # Iniciar el sonido cuando una canoa avanza
            sound_canoas.play()
            for _ in range(15):
            #for _ in range(30):
                start_p += 15
                #start_p +=30
                xxx2 = start_p 
                advance_canoa_green.place(x=xxx2, y=460)
                screen_canoas.update()
                screen_canoas.after(30)
                # Sumarle 200 puntos despues de que el jugador avance
                clasification_da["Canoa Green"] += 20
                if xxx2 >= finish_li:                 
                    # Esconder a todos los jugadores
                    advance_canoa_green.place_forget()
                    advance_canoa_red.place_forget()
                    advance_canoa_purple.place_forget()
                    gif_crocodile.place_forget()
                    # Establecer al ganador en la linea de meta
                    advance_canoa_green.place(x=1240,y=460)
                    w = "Canoa Green"
                    # Ir a la siguiente ronda
                    reset_rou()
                    break
        
        # Si el tercer jugador constesto bien, entonces avanzar jugador
        elif tu == 3:
            start_p = xxx3
            # Iniciar el sonido cuando una canoa avanza
            sound_canoas.play()
            for _ in range(15):
            #for _ in range(30):
                start_p += 15
                #start_p +=30
                xxx3 = start_p
                advance_canoa_purple.place(x=xxx3, y=560)
                screen_canoas.update()
                screen_canoas.after(30)
                # Sumarle 200 puntos despues de que el jugador avance
                clasification_da["Canoa Purple"] += 20
                if xxx3 >= finish_li:
                    # Esconder a todos los jugadores
                    advance_canoa_purple.place_forget()
                    advance_canoa_red.place_forget()
                    advance_canoa_green.place_forget()
                    gif_crocodile.place_forget()
                    # Establecer al ganador en la linea de meta
                    advance_canoa_purple.place(x=1240,y=560)
                    w = "Canoa Purple"
                    # Ir a la siguiente ronda
                    reset_rou()
                    break
        
        # Si continua es Falso entonces activar los botones de respuesta y poner al ganador de la ronda
        if contin==False:
            answ.config(state=NORMAL)
            answ2.config(state=NORMAL)
            answ3.config(state=NORMAL)
            answ4.config(state=NORMAL)
            messagebox.showinfo("Ganador", w + " ha ganado la ronda!")
            # Muestra la tabla de clasificacion
            screen_clasification(clasification_da)

    # Define la funcion para la opcion 1
    def opti1():
        # Hace el sonido al hacer click
        sound_click.play()
        global tu, xxx4, correc_answer_te
        # Desactiva los botones
        answ.config(state=DISABLED)
        answ2.config(state=DISABLED)
        answ3.config(state=DISABLED)
        answ4.config(state=DISABLED)
        
        # si la opcion es correcta entonces avanza jugador
        if corre == 1:
            player_advan()

        # Si la opcion no es correcta entonces avanza la ignorancia
        else:
            start_positi = xxx4
            #for _ in range(50):
            for _ in range (15):
                #start_positi += 50
                start_positi += 15
                xxx4 = start_positi
                gif_crocodile.place(x=xxx4, y=656)
                screen_canoas.update()
                screen_canoas.after(30)
                # Le suma 200 puntos a la ignorancia
                clasification_da["Crocodile"] += 20
                if xxx4 >= finish_li:
                    # Establece a la ignorancia en la linea de meta
                    gif_crocodile.place(x=1240, y=656)
                    messagebox.showinfo("Ganador", "Crocodile")
                    reset_rou()
                    break
            # Si la respuesta no es correcta mostrar el mensaje
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_te}")

        tu += 1
        if tu > 3:
            tu = 1
        str_ne.set(f"Jugador {tu}")
        # Avanza a la siguiente pregunta
        advance_to_next_questi()

    # Define la funcion para la opcion 2
    def opti2():
         # Hace el sonido al hacer click
        sound_click.play()
        global tu, xxx4, correc_answer_te
        # Desactiva los botones
        answ.config(state=DISABLED)
        answ2.config(state=DISABLED)
        answ3.config(state=DISABLED)
        answ4.config(state=DISABLED)
        
        # si la opcion es correcta entonces avanza jugador
        if corre == 2:
            player_advan()

        # Si la opcion no es correcta entonces avanza la ignorancia
        else:
            start_positi = xxx4
            #for _ in range(50):
            for _ in range (15):
                #start_positi += 50
                start_positi += 15
                xxx4 = start_positi
                gif_crocodile.place(x=xxx4, y=656)
                screen_canoas.update()
                screen_canoas.after(30)
                # Le suma 200 puntos a la ignorancia
                clasification_da["Crocodile"] += 20
                if xxx4 >= finish_li:
                    # Establece a la ignorancia en la linea de meta
                    gif_crocodile.place(x=1240, y=656)
                    messagebox.showinfo("Ganador", "Crocodile")
                    reset_rou()
                    break
            # Si la respuesta no es correcta mostrar el mensaje
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_te}")

        tu += 1
        if tu > 3:
            tu = 1
        str_ne.set("Jugador " + str(tu))
        # Avanza a la siguiente pregunta
        advance_to_next_questi()

    # Define la funcion para la opcion 3
    def opti3():
        # Hace el sonido al hacer click
        sound_click.play()
        global tu, xxx4, correc_answer_te
        # Desactiva los botones
        answ.config(state=DISABLED)
        answ2.config(state=DISABLED)
        answ3.config(state=DISABLED)
        answ4.config(state=DISABLED)
        
        # si la opcion es correcta entonces avanza jugador
        if corre == 3:
            player_advan()

        # Si la opcion no es correcta entonces avanza la ignorancia
        else:
            start_positi = xxx4
            #for _ in range(50):
            for _ in range (15):
                #start_positi += 50
                start_positi += 15
                xxx4 = start_positi
                gif_crocodile.place(x=xxx4, y=656)
                screen_canoas.update()
                screen_canoas.after(30)
                # Le suma 200 puntos a la ignorancia
                clasification_da["Crocodile"] += 20
                if xxx4 >= finish_li:
                    # Establece a la ignorancia en la linea de meta
                    gif_crocodile.place(x=1240, y=656)
                    messagebox.showinfo("Ganador", "Crocodile")
                    reset_rou()
                    break
            # Si la respuesta no es correcta mostrar el mensaje
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_te}")
        tu += 1
        if tu > 3:
            tu = 1
        str_ne.set("Jugador " + str(tu))
        # Avanza a la siguiente pregunta
        advance_to_next_questi()

    # Define la funcion para  la opcion 4
    def opti4():
          # Hace el sonido al hacer click
        sound_click.play()
        global tu, xxx4, correc_answer_te
        # Desactiva los botones
        answ.config(state=DISABLED)
        answ2.config(state=DISABLED)
        answ3.config(state=DISABLED)
        answ4.config(state=DISABLED)
        
        # si la opcion es correcta entonces avanza jugador
        if corre == 4:
            player_advan()

        # Si la opcion no es correcta entonces avanza la ignorancia
        else:
            start_positi = xxx4
            #for _ in range(50):
            for _ in range (15):
                #start_positi += 50
                start_positi += 15
                xxx4 = start_positi
                gif_crocodile.place(x=xxx4, y=656)
                screen_canoas.update()
                screen_canoas.after(30)
                # Le suma 200 puntos a la ignorancia
                clasification_da["Crocodile"] += 20
                if xxx4 >= finish_li:
                    # Establece a la ignorancia en la linea de meta
                    gif_crocodile.place(x=1240, y=656)
                    messagebox.showinfo("Ganador", "Crocodile")
                    reset_rou()
                    break
            # Si la respuesta no es correcta mostrar el mensaje
            else:
                messagebox.showinfo("Incorreco", f"La respuesta correca era: {correc_answer_te}")
        tu += 1
        if tu > 3:
            tu = 1
        str_ne.set("Jugador " + str(tu))
        # Avanza a la siguiente pregunta
        advance_to_next_questi()

    # Define la funcion para ir a la siguiente ronda
    def reset_rou():
        # Detiene el sonido de las canoas
        sound_canoas.stop()
        # Toma las variables globales
        global xxx1, xxx2, xxx3, xxx4, corre, tu, used_questi, roun, rouns_lim, contin, w, button_end_game, button_other_round

        # Reinicia las posiciones de x de los jugadores
        xxx1 = 40
        xxx2 = 40
        xxx3 = 40
        xxx4 = 40
            
        # Reinicia la posicion de los jugadores
        gif_crocodile.place(x=xxx4, y=650)
        advance_canoa_red.place(x=xxx1, y=360)
        advance_canoa_green.place(x=xxx2, y=460)
        advance_canoa_purple.place(x=xxx3, y=560)

        # Reinicia el turno y el ganador
        tu = 0
        w = ""
        # Habilita los botones
        answ.config(state=NORMAL)
        answ2.config(state=NORMAL)
        answ3.config(state=NORMAL)
        answ4.config(state=NORMAL)
        str_ne.set(f"Jugador {tu}")

        # Si la variable rounds es igual o mayor a rounds limit entonces calcular quien fue el que tuvo mas puntos
        if roun >= rouns_lim:
            max_score = max(clasification_da.values())
            winners = [key for key, value in clasification_da.items() if value == max_score]
            
            if len(winners) == 1:
                winner_game = winners[0]
                # Si gano la ignorancia entonces poner el gif de game over y el sonido de derrota
                if winner_game == "Crocodile":
                    sound_canoas.stop()
                    animation_gameover = GIFWinnerCocodrile(screen_canoas, "visual/gifs/animations_win/win_cocodrile.gif")
                    animation_gameover.place(x=400, y=200)
                    animation_gameover.play()
                    sound_defeat.play()

                    button_end_game_image = PhotoImage(file=r"visual/images/buttons_images/buttons_canoas/Boton_Terminar_Partida.png")
                    button_end_game = Button(screen_canoas,image=button_end_game_image,command=end_game_button_action,bg="Black")
                    button_end_game.place(x=680, y=420)

                # Si gano un jugador entonces poner el sonido de victoria y mostrar un mensaje de quien fue el ganador
                else:
                    sound_canoas.stop()
                    sound_win.play()
                    
                    animation_victory = GIFCanoas(screen_canoas, "visual/gifs/animations_win/win_canoa.gif")
                    animation_victory.place(x=400, y=200)
                    animation_victory.play
                    
                    button_end_game_image = PhotoImage(file=r"visual/images/buttons_images/buttons_canoas/Boton_Terminar_Partida.png")
                    button_end_game = Button(screen_canoas,image=button_end_game_image,command=end_game_button_action,bg="Black")
                    button_end_game.place(x=680, y=500)
                    
                    messagebox.showinfo("¡Ganador del juego!", f"El ganador del juego es: {winner_game}")
            # Si fue un empate entonces mostrar el mensaje de quien y quien fue el empate
            else:
                messagebox.showinfo("Empate", f"¡Hay un empate entre los siguientes jugadores: {', '.join(winners)}!")
            # Llama a la funcion de la pantalla de clasificacion
            screen_clasification(clasification_da)
        # Si no es ninguno de los anteriores  entonces mostrar una nueva ronda
        else:
            roun += 1
            messagebox.showinfo("Nueva ronda", f"Inicia la ronda {roun}")
            select_questi()

    # Funcion para el boton de terminar partida, que aparece al finalizar un juego
    def end_game_button_action():
        global button_end_game
        if button_end_game:
            # Despues de que el boton es presionado se destruye
            button_end_game.destroy()
        # Se destruye la pantalla de canoas
        screen_canoas.destroy()
    
    # Define la funcion para avanzar a la siguiente pregunta
    def advance_to_next_questi():
        # Toma variables globales
        global roun, contin

        # Usa un ciclo for para verificar que la pregunta no a sido usada
        if len([questi for questi in selecti if questi[0] not in used_questi]) > 0:
            select_questi()
        # Verifica que rounds sea menor que 1, y si lo es entonces mostrar mensaje
        else:
            roun += 1
            if roun < 1:
                messagebox.showinfo("Comienza la ronda"+ roun + 1)
                used_questi.clear()
                select_questi()
            # Si no mostrar que ya no hay preguntas disponibles y quitar las opciones
            else:
                str_questi.set("Ya no hay preguntas disponibles")
                str_answ1.set("")
                str_answ2.set("")
                str_answ3.set("")
                str_answ4.set("")

                # Desactivar los botones de respuesta
                for btn in [answ, answ2, answ3, answ4]:
                    if btn.winfo_exists():
                        btn.config(state=DISABLED)
    
    # Define la funcion para seleccionar las preguntas
    def select_questi():
        # Toma variables globales
        global corre, correc_answer_te
        # Crea un ciclo for para revisar las preguntas que no han sido usadas
        unused_questio = [questi for questi in selecti if questi[0] not in used_questi]

        
        if unused_questio:
            # Elige una pregunta aleatoria de las que no han sido usadas
            question_dat = random.choice(unused_questio)
            used_questi.append(question_dat[0])
            str_questi.set(question_dat[2])
            str_answ1.set(question_dat[3])
            str_answ2.set(question_dat[4])
            str_answ3.set(question_dat[5])
            str_answ4.set(question_dat[6])
            corre = question_dat[7]
            # Variable para mostrar la respuesta correcta
            correc_answer_te = question_dat[2 + corre]

            answ.config(state=NORMAL)
            answ2.config(state=NORMAL)
            answ3.config(state=NORMAL)
            answ4.config(state=NORMAL)
        # Si no mostrar que ya no hay preguntas disponibles
        else:
            str_questi.set("Ya no hay preguntas disponibles")
            str_answ1.set("")
            str_answ2.set("")
            str_answ3.set("")
            str_answ4.set("")
            
            for btn in [answ, answ2, answ3, answ4]:
                if btn.winfo_exists():
                    btn.config(state=NORMAL)
                    
    # Define la funcion answ
    def asnw(eve):
        global selecti
        # Obtiene el valor de la categoria
        c = eve.widget.get()
        # Reemplaza los espacios por guiones bajos
        c=str(c).replace("_"," ")
        selecti = recover_questions(c)
        select_questi()
    
    # Define la funcion de seleccionar todas las preguntas
    def select_all_questio():
        global selecti
        # Hace el sonido al hacer click
        sound_click.play()
        # llama a la funcion para recuperar todas las preguntas
        all_questio = recover_questions("all")
        selecti = all_questio
        select_questi()

    # Define la funcion para editar las categorias
    def edit_categori():
        sound_click.play()
        screen_categories()
    
    # Define la funcion para terminar el juego
    def end_ga():
        # Hace el sonido al hacer click
        sound_click.play()
        # Destruye la pantalla de canoas
        screen_canoas.destroy()
    
    # Recupera las categorias
    l_categori = recover_categories()
    # Toma las categorias como un vector vacio
    cs = []
    for c in l_categori:
        ca2=str(c[0])
        cs.append(ca2)

    # Inicia el mixer de pygame
    pygame.init()
    pygame.mixer.init()
    
    # Define los efectos de sonido con la libreria de pygame
    sound_defeat = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/FIn_del_juego.mp3")
    sound_defeat.set_volume(1.0)

    sound_win = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/Jugador_Gano.mp3")
    sound_win.set_volume(1.0)
    
    sound_canoas = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/Para_Canoas.mp3")
    sound_canoas.set_volume(1.0)
    
    sound_click = pygame.mixer.Sound("music/Efectos_de_Sonido_Juego/Sonido_al_hacer_click.mp3")
    sound_click.set_volume(1.0)

    # Define el fondo de pantalla
    background_canoas_image = PhotoImage(file=r"visual/images/backgrounds_game/fondo_canoas.png")
    background_canoas = Label(screen_canoas, image=background_canoas_image, bg="Green")
    background_canoas.place(x=1,y=1)

    # Define la pista de las canoas tomandola como un gif y poniendole un fondo verde
    track_canoas = GIFTrack(screen_canoas,  "visual/images/tracks_images/canoas_pist.gif")
    track_canoas.config(bg="#4887e4")
    track_canoas.place(x=10,y=350)

    # Define la etiqueta de la categoria con un fondo verde
    etiquet_cateogories_image = PhotoImage(file=r"visual/images/buttons_images/buttons_canoas/Category.png")
    etiquet_cateogories = Label(screen_canoas, image=etiquet_cateogories_image,bg="#008f39")
    etiquet_cateogories.place(x=8, y=40)

    # Define la combobox de las categorias con un formato de Arial 12
    categors = ttk.Combobox(screen_canoas, font="Helvetica 18 bold")
    categors["values"]=cs
    categors["font"]=("Arial", 18)
    screen_canoas.option_add("*TCombobox*Listbox.font", ("Arial", 12))
    categors.place(x=145, y=40)
    categors.bind("<<ComboboxSelected>>", asnw)
    
    # Define la imagen del catalogo con un fondo verde
    image_catalo = Image.open("visual/images/buttons_images/button_catalog.png").convert("RGBA")
    bg_canoas_color = Image.new("RGBA", image_catalo.size, screen_canoas["bg"])  
    image_bg = Image.alpha_composite(bg_canoas_color, image_catalo)  

    image_catalo_tk = ImageTk.PhotoImage(image_bg)

    label_image_catalo = tk.Label(screen_canoas, image=image_catalo_tk, bg="#00aae4")
    
    # Define la posicion del boton de catalogo
    button_catal=Button(screen_canoas, image=image_catalo_tk, command=edit_categori,bg="#008f39")
    button_catal.place(x=1000, y=30)

    # Define la etiqueta de mostrar el turno del jugador
    str_ne.set("Jugador 1")
    next_play = Label (screen_canoas,bg="#008f39",textvariable=str_ne,font="Helvetica 18 bold")
    next_play.place(x=800,y=40)

    # Define la etiqueta de las preguntas, con un fondo verde
    question_etiqu_image = PhotoImage(file=r"visual/images/buttons_images/buttons_canoas/Question.png")
    question_etiqu = Label(screen_canoas, bg="#008f39", image=question_etiqu_image)
    question_etiqu.place(x=8, y=90)

    # Define lo que va a dentro de la stringVar de la pregunta
    str_questi.set("")
    quest = Label(screen_canoas, textvariable=str_questi, font="Helvetica 18 bold", bg="Lavender", width=60, wraplength=900, justify=LEFT)
    quest.place(x=145, y=90)

    # Define el boton de todas las preguntas y su fondo de color verde
    button_all_questi_image = PhotoImage(file=r"visual/images/buttons_images/buttons_canoas/Button_all.png")
    button_all_questi = Button(screen_canoas, image=button_all_questi_image, command=select_all_questio, bg="#008f39")
    button_all_questi.place(x=500, y=40)

    # Define los botones de las respuestas tanto sus comandos como sus colores y longitud
    str_answ1.set("")
    answ = Button(screen_canoas, textvariable=str_answ1, command=opti1, font="Helvetica 14 bold", bg="#20603d", width=70,justify=LEFT)
    answ.place(x=200, y=150)
    
    str_answ2.set("")
    answ2 = Button(screen_canoas, textvariable=str_answ2, command=opti2, font="Helvetica 14 bold", bg="#20603d", width=70,justify=LEFT)
    answ2.place(x=200, y=192)
    
    str_answ3.set("")
    answ3 = Button(screen_canoas, textvariable=str_answ3, command=opti3, font="Helvetica 14 bold", bg="#20603d", width=70,justify=LEFT)
    answ3.place(x=200, y=235)

    str_answ4.set("")
    answ4 = Button(screen_canoas, textvariable=str_answ4, command=opti4, font="Helvetica 14 bold", bg="#20603d", width=70,justify=LEFT)
    answ4.place(x=200, y=280)

    # Define el boton de terminar partida que se encuentra en la parte superior de la pantalla de canoas
    button_l = tk.Button(screen_canoas, text="Terminar Partida", command=end_ga, font="Helvetica 9 bold", width=200, bg="#594126",fg="White")
    button_l.place(x=1, y=1) 
    
    # Define a los jugadores como GIFS tanto sus posiciones y el color de su fondo
    advance_canoa_red=GIFCanoas(screen_canoas, "visual/images/players_images/canoas/Player1.gif")
    advance_canoa_red.config(bg="#4887e4")
    advance_canoa_red.place(x=xxx1,y=360)
    advance_canoa_red.play()
    
    advance_canoa_green=GIFCanoas(screen_canoas,"visual/images/players_images/canoas/Player2.gif")
    advance_canoa_green.config(bg="#4887e4")
    advance_canoa_green.place(x=xxx2,y=460)
    advance_canoa_green.play()
    
    advance_canoa_purple=GIFCanoas(screen_canoas, "visual/images/players_images/canoas/Player3.gif")
    advance_canoa_purple.config(bg="#4887e4")
    advance_canoa_purple.place(x=xxx3,y=560)
    advance_canoa_purple.play()

    # Define la animacion del cocodrilo como un GIF tanto su posicion como el color de su fondo
    gif_crocodile = GIFCrocodile(screen_canoas, "visual/images/players_images/canoas/Crocodile_Ignorance.gif")
    gif_crocodile.config(bg="#4887e4")
    gif_crocodile.place(x=xxx4,y=656)
    gif_crocodile.play()
    
    # Define el boton de clasificacion como una images, asi tambien su posicion y el color de fondo
    button_clasificati_image = PhotoImage(file=r"visual/images/buttons_images/buttons_canoas/Button_points.png")
    button_clasificati = tk.Button(screen_canoas, image=button_clasificati_image, command=lambda:screen_clasification(clasification_da), bg="#008f39")
    button_clasificati.place(x=1100, y=40)
    
    # Ejecuta la pantalla
    screen_canoas.mainloop()