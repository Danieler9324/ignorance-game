# Crea la clase Button
class Button:
    #Crea el constructor de la clase button, para definir sus propiedades
    def __init__(self, text, pos, font, base_color, hovering_color):
        self.text = text
        self.pos = pos
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.current_color = base_color
        self.text_surface = self.font.render(self.text, True, self.base_color)
        self.rect = self.text_surface.get_rect(center=self.pos)

    # Crea una funcion para actualizar el boton dependiendo del evento solicitado
    def update(self, screen):
        self.text_surface = self.font.render(self.text, True, self.current_color)
        screen.blit(self.text_surface, self.rect)

    # Crea una funcion para revisar si el button a sido presionado
    def check_for_input(self, position):
        return self.rect.collidepoint(position)

    # Crea una funcion si el cursor esta encima del boton, entonces cambiar de color
    def change_color(self, position):
        if self.check_for_input(position):
            self.current_color = self.hovering_color
        else:
            self.current_color = self.base_color