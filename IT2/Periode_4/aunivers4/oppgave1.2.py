import pygame as pg  
import random as rnd  


def random_sirkel():
    vindu = pg.display.set_mode([900,900])

    continue_game = True
    posisjon = (rnd.randint(0,900), rnd.randint(0,900))
    radius = rnd.randint(10,1000)
    while continue_game: 
        for event in pg.event.get(): 
            if event.type == pg.QUIT: continue_game = False
    
        vindu.fill((255,255,255))

        pg.draw.circle(vindu, (255,0,0), posisjon, radius)

        pg.display.flip()

    pg.quit()

random_sirkel()