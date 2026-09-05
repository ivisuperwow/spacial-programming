import pygame
from pgzero.actor import Actor
from pgzero.loaders import images
from config import WIDTH, HEIGHT
from game.bullet import Bullet

class Player:
    def __init__(self):
        # -------------------------------------------------------------
        # SEMANA 1: ATRIBUTOS DE LA NAVE
        # -------------------------------------------------------------
        # ACTIVIDAD 1: Define aca tus propios atributos usando 'self.'
        # Pista: Revisar WEEK1.md cuando termines de escribir los atributos notaras que tu nave aparecera en pantalla, pero aun no se podra mover
        # Es posible que te salgan errores en la terminal como "AttributeError: 'Player' object has no attribute 'width'" esto es una pista de lo que te falta, solo pon self. seguido del atributo que te falta :)
        self.width = 60
        self.height = 40
        self.position_player_x = 100
        self.position_player_y = 300
        self.speed = 10
        self.score = 0
        self.lives = 3
        self.cooldown = 10 
        self.cooldown_timer = 0
        # -------------------------------------------------------------
        # Descarga tu propia imagen de nave y guárdala en la carpeta 'images/player/'.
        # Luego, reemplaza "player/spaceship" por el nombre de tu archivo (sin .png o .jpg, o la extension que tenga).
        # -------------------------------------------------------------
        imagen_name = "player/mi_nave"

        surf = images.load(imagen_name)
        surf = pygame.transform.scale(surf, (self.width, self.height))
        
        self.actor = Actor(imagen_name, (self.position_player_x, self.position_player_y))
        self.actor._surf = surf
        self.actor._orig_surf = surf
        self.actor._update_pos()

    def move(self, keyboard, keys):
        # -------------------------------------------------------------
        # PROGRAMAR MOVIMIENTO
        # Recuerda la lógica del eje de coordenadas en la pantalla:
        # - Para subir: restamos en Y
        # - Para bajar: sumamos en Y
        # - Para la izquierda: restamos en X
        # - Para la derecha: sumamos en X
        # -------------------------------------------------------------

        # Ejemplo: Mover hacia arriba al presionar la tecla UP
        if keyboard[keys.UP]:
            self.actor.y -= self.speed

        # Completa el movimiento para las demás direcciones:
        # - Mover hacia abajo

        # - Mover hacia la izquierda

        # - Mover hacia la derecha

        if keyboard[keys.UP]:
            self.actor.y -= self.speed

        # Abajo (Flecha Abajo)
        if keyboard[keys.DOWN]:
            self.actor.y += self.speed

        # Izquierda (Flecha Izquierda)
        if keyboard[keys.LEFT]:
            self.actor.x -= self.speed

        # Derecha (Flecha Derecha)
        if keyboard[keys.RIGHT]:
            self.actor.x += self.speed


        # -------------------------------------------------------------
        # LÍMITES DE LA PANTALLA (Semana 1)
        # -------------------------------------------------------------
        half_width = self.width // 2
        half_height = self.height // 2

        if self.actor.x < half_width:
            self.actor.x = half_width
        if self.actor.x > WIDTH - half_width:
            self.actor.x = WIDTH - half_width
        if self.actor.y < half_height:
            self.actor.y = half_height
        if self.actor.y > HEIGHT - half_height:
            self.actor.y = HEIGHT - half_height

    def draw(self):
        self.actor.draw()

    # -----------------------------------------------------------------
    # SEMANA 2: DISPAROS Y RECARGA
    # -----------------------------------------------------------------
    def update_cooldown(self):
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1

    def shoot(self):
        if self.cooldown_timer <= 0:
            # 2. Reiniciar el reloj de recarga
            self.cooldown_timer = self.cooldown
        
            # 3. Calcular la punta de la nave (X e Y)
            bullet_x = self.actor.x + (self.width // 2)
            bullet_y = self.actor.y
            
            # 4. Crear y retornar el objeto Bullet
            return Bullet(bullet_x, bullet_y)
    
        return None    

    # -----------------------------------------------------------------
    # RECIBIR DAÑO Y DAÑO A ENEMIGOS
    # -----------------------------------------------------------------
    def take_damage(self):
        self.lives -= 1
        return self.lives <= 0


