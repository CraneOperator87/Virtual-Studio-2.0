import pygame as pg  

pg.init()

vindu = pg.display.set_mode([750, 750]) # Første verdi -> Bredde, Andre verdi -> Høyde
font = pg.font.SysFont("Calibri", 24)   # Font "Calibri", størelse "24"

# Finne ut om spillet har blitt lukket:
continue_game = True
while continue_game:
    # Fortsetter å kjøre spillet:
    for event in pg.event.get():
        if event.type == pg.QUIT: # Hvis brukeren lukker vinduet -> avslutt spillet
            continue_game = False

    vindu.fill((255, 255, 255)) # Farger vinduet hvitt (RGB: 255,255,255)

    pg.draw.circle(vindu,(255, 0, 0),(375, 375), 50)  # Tegner en sirkel, med farge (RGB: 255,0,0) -> Rød, posisjon (100,250), radius 50

    pg.display.flip() # Oppdaterer alt innholdet i vinduet

pg.quit() # Avslutter pygame