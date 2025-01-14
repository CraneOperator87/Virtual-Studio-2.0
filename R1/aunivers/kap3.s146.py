from pylab import *  # Importerer alle funksjoner og moduler fra pylab-biblioteket

delta_x = 1E-8  # Definerer en verdi for delta_x

def f(x):  # Definerer en funksjon f som tar inn en parameter x
  return x**2 + 2*x  # Returnerer verdien av x^2 + 2*x

def derivert(a):  # Definerer en funksjon derivert som tar inn en parameter a
  return (f(a + delta_x) - f(a)) / delta_x  # Returnerer den deriverte av f ved a

x_verdier = linspace(-5, 5, 100)  # Genererer en array med 100 jevnt fordelte verdier fra -5 til 5
y_verdier = f(x_verdier)  # Beregner verdiene av f for hver verdi i x_verdier
dy_verdier = derivert(x_verdier)  # Beregner verdiene av den deriverte av f for hver verdi i x_verdier

plot(x_verdier, y_verdier)  # Plotter x_verdier mot y_verdier
plot(x_verdier, dy_verdier)  # Plotter x_verdier mot dy_verdier
show()  # Viser plottene