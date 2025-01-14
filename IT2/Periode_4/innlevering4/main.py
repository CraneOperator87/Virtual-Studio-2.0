import pygame
import random

WIDTH = 800 # Bredde på vinduet
HEIGHT = 600 # Høyde på vinduet
BLACK = (0, 0, 0) # Farge : Sort
GREEN = (0, 255, 0) # Farge : Grønn
YELLOW = (255, 255, 0) # Farge : Gul
GRAY = (128, 128, 128) # Farge : Grå
WHITE = (255, 255, 255) # Farge : Hvit

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Vidnuet vårt (Spillbrett)
pygame.display.set_caption("PacTroll") # Navnet til vidneut

class Troll(pygame.sprite.Sprite):  # Troll klassen, (Spilleren),en del av en liste med objekter der spillet velger å tegne alle deler uten å trenge å loope det.
    def __init__(self):
        """Initialiserer Troll klassen."""
        super().__init__()
        self.image = pygame.Surface((50, 50)) # Selve figuren, størrelse 50 x 50
        self.image.fill(GREEN)  # Fargen til figuren som er grønn
        self.rect = self.image.get_rect() # Rektangelet som figuren er i 
        self.rect.center = (WIDTH // 2, HEIGHT // 2) # Plasseringen til figuren, slik at den ALLTID starter i sentrum av skjermen, uavhengig av skjermstørrelse
        self.speed = 1 # Fart til trollet

    def update(self):
        """Bruker input"""
        keys = pygame.key.get_pressed() # Henter input fra brukeren:
        if keys[pygame.K_UP]: self.rect.y -= self.speed           # Hvis brukeren trykker på piltasten opp -> flytt figuren opp
        elif keys[pygame.K_DOWN]: self.rect.y += self.speed       # Hvis brukeren trykker på piltasten ned -> flytt figuren ned  
        elif keys[pygame.K_LEFT]: self.rect.x -= self.speed      # Hvis brukeren trykker på piltasten venstre -> flytt figuren til venstre
        elif keys[pygame.K_RIGHT]: self.rect.x += self.speed     # Hvis brukeren trykker på piltasten høyre -> flytt figuren til høyre

        self.rect.clamp_ip(screen.get_rect()) # Sørger for at figuren ikke går utenfor skjermen, denne måtte jeg søke opp det er NO WAY auinvers hadde "klart å forklare dette til meg"
                                              #  hadde aldri klart å finne ut av dette selv

class Food(pygame.sprite.Sprite):  # Samme prinsipp som trollet, vi lager det i en liste, pygame.sprite.Sprite 
    def __init__(self, x, y):  
        """Initialiserer Food (mat) klassen."""
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Initialiserer Obstacle (hindring) klassen."""
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()  # Starter spillet
clock = pygame.time.Clock() 
clock.tick(60) # Setter en grense på 60 FPS (Frames Per Second)

troll = Troll() # Lager en instans av Troll klassen
foods = pygame.sprite.Group() # Lager en gruppe for mat, som sagt, dette er pygame.sprite.Sprite brukt i praksis. Den tegner alle delene uten å trenge å loope det.
obstacles = pygame.sprite.Group() # Lager en gruppe for hindringer, samme her, pygame.sprite.Sprite brukt i praksis. Den tegner alle delene uten å trenge å loope det.

all_sprites = pygame.sprite.Group() # Lager en gruppe for alle sprites (alle objekter)
all_sprites.add(troll) # Legger til trollet i gruppen med alle sprites (alle andre objekter)

for _ in range(3):  # Vi skal ha tre matbiter, vi kaller det egentlig hva vi vil
    while True:
        food_x = random.randint(0, WIDTH - 20) # Lager maten på tilfeldige plasser
        food_y = random.randint(0, HEIGHT - 20) # Lager maten på tilfeldige plasser
        food = Food(food_x, food_y) # Lager en instans av Food klassen og viser oss maten
        if not pygame.sprite.spritecollide(food, all_sprites, False): # Sjekker om maten kolliderer med andre objekter
            foods.add(food) # Legger til maten i gruppen med mat
            all_sprites.add(food) # Legger til maten i gruppen med alle sprites (alle andre objekter) -> slik at den blir tegnet
            break

score = 0 # Scoren til spilleren
font = pygame.font.Font(None, 36) # Random font, og størrelse 36

running = True # Spillet kjører
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: running = False 

    all_sprites.update() # Oppdaterer alle sprites (alle objekter) -> slik at de flytter seg, men siden spiller er den som kan "bevege" seg så opptateres bare trolelt

    food_collisions = pygame.sprite.spritecollide(troll, foods, True)
    for food_collision in food_collisions:
        obstacle = Obstacle(food_collision.rect.x, food_collision.rect.y)
        obstacles.add(obstacle)
        all_sprites.add(obstacle)

        while True:
            food_x = random.randint(0, WIDTH - 20)
            food_y = random.randint(0, HEIGHT - 20)
            food = Food(food_x, food_y)
            # Den store forskjellen mellom denne og "maten" over er at vi sjekker om maten er på brettet i det vi starter spillet
            if not pygame.sprite.spritecollide(food, all_sprites, False): # Sjekker om maten kolliderer med andre objekter 
                foods.add(food)
                all_sprites.add(food)
                break

        troll.speed += 0.1 # Øker farten til trollet når han spiset en mat
        score += 1 # Legger til 1 i score

    obstacle_collisions = pygame.sprite.spritecollide(troll, obstacles, False) # Hvis trollet spiser en mat, så blir det en hindring
    if obstacle_collisions: # Hvis trollet kolliderer med en hindring
        running = True # Her tror det skal stå False, men siden jeg ikke aner hva jeg skal gjøre for at spillet ikke kræsjer med en gang så blir det stående på True

    screen.fill(BLACK) # Farger skjermen svart
    all_sprites.draw(screen) # Tegner alle sprites (alle objekter) på skjermen

    score_text = font.render("Score: " + str(score), 1, WHITE) # Lager en tekst som viser scoren
    screen.blit(score_text, (10, 10)) # Legger til teksten på skjermen

    pygame.display.flip()

pygame.quit() # Avslutter spillet