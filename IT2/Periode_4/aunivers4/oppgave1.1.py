import pygame as pg  

def main():
    # Initialiserer pygame
    pg.init()

    vindu = pg.display.set_mode([400,300]) # Første verdi -> Bredde, Andre verdi -> Høyde

    continue_game = True 
    while continue_game: 
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                continue_game = False
            
        vindu.fill((255, 255, 255))
        pg.draw.rect(vindu, (243, 203,50), (0, 0, 400, 100)) # Gul rektangel
        pg.draw.rect(vindu, (60, 160, 25), (0, 100, 400, 100)) # Grønn rektangel
        pg.draw.rect(vindu, (190, 40, 11), (0, 200, 400, 100)) # Rød rektangel

        pg.display.flip()
    
    pg.quit()

main()