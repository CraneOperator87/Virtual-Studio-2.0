def funksjonsNavn():
    # Beskrivelse til funksjonen
    """Her er docstring, dokumenterende tekst!"""
    # Funksjonen sin oppgave:
    print("Hello world!")

def siHei():
  """En funksjon som sier hei i konsollen"""
  print("\nHei\n")

siHei()


# Vrien bruk av funksjon uten parameter
lengde1 = 4
bredde1 = 8
def Arealrektangel():
   return lengde1 * bredde1

print(f"Lengden {lengde1} og bredde {bredde1} er: {Arealrektangel()}")


# Bruk av parametere 
def arealrektangel(lengde, bredde):
   """En funksjon som regner ut lengden og bredden i en rektangel"""
   return lengde * bredde
   
print(f"Arealet med lengde 4 og bredde 8, får vi arealet {arealrektangel(4,8)}")


print("\n\n\033[91mprogramslutt\033[0m")