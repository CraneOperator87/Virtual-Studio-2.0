from pylab import *  # Importerer alle funksjoner og klasser fra pylab-modulen

lengde = array([20, 40, 60, 80, 100])  # Oppretter en array med lengdeverdier
y_snitt = array([1.33, 2.06, 2.74, 3.26, 3.69])  # Oppretter en array med gjennomsnittsverdier
SE = array([0.06, 0.07, 0.08, 0.04, 0.05])  # Oppretter en array med standardavviksverdier

# Plotter blå prikker basert på lengde og gjennomsnittsverdier
plot(lengde, y_snitt, "b.")

# Plotter røde vertikale linjer basert på lengde, gjennomsnittsverdier og standardavviksverdier
vlines(lengde, y_snitt - 2*SE, y_snitt + 2*SE, "r")

xlabel("Lengde (cm)")  # Setter navn på x-aksen
ylabel("Tid (sekunder)")  # Setter navn på y-aksen

show()  # Viser plottet