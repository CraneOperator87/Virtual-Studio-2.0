import pygame as pg

clock = pg.time.Clock()
clock.tick(60)

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fart = fart
    self.radius = radius
    self.vindusobjekt = vindusobjekt
    self.farge = farge
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, (self.farge), (self.x, self.y), self.radius) 

  def flytt_y(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.y- self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()): self.fart = -self.fart
    
    # Flytter ballen
    self.y += self.fart
  
  def flytt_x(self):
     
    if ((self.x- self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()): self.fart = -self.fart

    self.x += self.fart
# Initialiserer/starter pygame

pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 920
VINDU_HOYDE  = 920
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

# Lager et Ball-objekt
ball1 = Ball(460, 460, -0.5, 25, (0,100,100),  vindu)
ball2 = Ball(460, 460, 0.5, 25, (100, 0, 100), vindu)
ball3 = Ball(460, 460, 0.5, 25, (100, 100, 0), vindu)
ball4 = Ball(460, 460, -0.5, 25, (100, 100, 100), vindu)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    vindu.fill((255, 255, 255))

    # Tegner og flytter ballen
    ball1.tegn(); ball1.flytt_y()
    ball2.tegn(); ball2.flytt_x()
    ball3.tegn(); ball3.flytt_y()
    ball4.tegn(); ball4.flytt_x()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()