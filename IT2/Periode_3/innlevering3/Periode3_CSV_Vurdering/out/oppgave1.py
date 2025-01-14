import csv
import os
import numpy as np
import matplotlib.pyplot as plt

# Filnavn
fil= "datasett/Medier.csv"
def main():

    årstall = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]  # Årstallene
    minutter = [] # Liste for minutter
    navn = []     # Liste for navn
    
    with open(fil, "r", encoding="utf-8") as file: # Åpner og leser filen
        data = csv.reader(file, delimiter=";")     # Leser filen og ignorerer semikolon
        next(data)                                 # Hopper over første rad       
        next(data)                                 # Hopper over andre rad
        next(data)                                 # Hopper over tredje rad
        for rad in data:                           # For hver rad i filen
            navn.append(rad[0])                    # Legger til navn ved å bruke rad[0], som er det første elemtentet i raden => navnet til media  
            minutter.append([np.nan if x in ['.', '..'] else float(x) for x in rad[1:]]) # Legger til minutter ved å bruke rad[1:], 
                                                                                         # som er resten av elementene i raden => minutter for hvert år
    for i, label in enumerate(navn):
        plt.plot(årstall, minutter[i], label=label)
    plt.xlabel("Årstall") # Navn på x-aksen
    plt.ylabel("Minutter") # Navn på y-aksen
    plt.title("Mediebruk i Norge 2010-2019") # Selve titell
    plt.xticks(årstall)
    plt.grid() 
    plt.legend()

    filename =  "out/plot.jpg"
    plt.savefig(filename, format='jpeg')

    plt.show()
        
def bestemtekatogarier():
    årstall = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019] 
    minutter = [] 
    navn = []     
    # Hjemmepc 3
    # Internett 5
    # Bøker 9
    
    with open(fil, "r", encoding="utf-8") as file: 
        data = csv.reader(file, delimiter=";")     
        next(data)                                       
        next(data)                                 
        next(data)                                 
        for rad in data:                           
            navn.append(rad[0])                   
            minutter.append([np.nan if x in ['.', '..'] else float(x) for x in rad[1:]])

    for i in [3,5,9]:
        plt.plot(årstall, minutter[i], label=navn[i])
    plt.xlabel("Årstall") # Navn på x-aksen
    plt.ylabel("Minutter") # Navn på y-aksen
    plt.title("Mediebruk i Norge 2010-2019") # Selve titell
    plt.xticks(årstall)
    plt.grid() 
    plt.legend()

    filname = "out/plot2.jpg"
    plt.savefig(filname, format='jpeg')
    
    plt.show()

def internettforbruk():
    årstall = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019] 
    minutter = [] 
    navn = []   
    
    with open(fil, "r", encoding="utf-8") as file: 
        data = csv.reader(file, delimiter=";")     
        next(data)                                       
        next(data)                                 
        next(data)                                 
        for rad in data:                           
            navn.append(rad[0])                   
            minutter.append([np.nan if x in ['.', '..'] else float(x) for x in rad[1:]])
        
    # Index for internett = 5
    maksverdi = max(minutter[5])
    maksår = årstall[minutter[5].index(maksverdi)]
    print(f"Året med mest internettforbruk var {maksår} med {maksverdi} minutter")
    minstverdi = min(minutter[5])
    minstår = årstall[minutter[5].index(minstverdi)]
    print(f"Året med minst internettforbruk var {minstår} med {minstverdi} minutter")
    

internettforbruk()
