from pylab import *  # Importing the pylab module, which provides a MATLAB-like interface for plotting

lengde = array([20, 40, 60, 80, 100])  # Creating an array of length values
y_snitt = array([1.33, 2.06, 2.74, 3.26, 3.69])  # Creating an array of average time values
SE = array([0.06, 0.07, 0.08, 0.04, 0.05])  # Creating an array of standard error values

plot(lengde, y_snitt, "b.")  # Plotting the length values against the average time values as blue dots
vlines(lengde, y_snitt - 2*SE, y_snitt + 2*SE, "r")  # Plotting vertical red lines representing the range of values (average time ± 2*SE)

xlabel("Lengde (cm)")  # Setting the label for the x-axis
ylabel("Tid (sekunder)")  # Setting the label for the y-axis

x = linspace(10, 110, 100)  # Creating an array of 100 evenly spaced values between 10 and 110
y = 0.195*x**0.6413  # Calculating the corresponding y-values using a mathematical formula
plot(x, y, "--")  # Plotting the calculated values as a dashed line

show()  # Displaying the plot
