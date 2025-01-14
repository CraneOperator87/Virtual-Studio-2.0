tekst = "Datamaskiner er ubrukelige. De kan bare gi oss svar."

"""
print(tekst[:13]," ", tekst[])...          # Her kunne jeg ha fortsatte, men det er ikke fornuftig fordi det tar rimelig lengere tid enn annet metode
"""

"""
tekst1 = tekst.replace("er","")            # For hver gang jeg "replacer" et ord, definerer jeg ny "Tekst" som "tekst1" og "tekst2" osv
tekst2 = tekst1.replace("ubrukelige.","")  # Jeg får fjerna enkelte ord som jeg ikke trenger.
tekst3 = tekst2.replace("De","")
tekstFinal= tekst3.replace("bare","")      
"""
tekstFinal = tekst.replace("er","").replace("ubrukelige.","").replace("De","").replace("bare","") # Jeg finner ut at jeg kan sammenslå "replace" og trenger ikke å bruke 4 linjer
                                                                                                  # For å fjerne enkelte ord fra teksten.
tekstFinal = " ".join(tekstFinal.split())  # Dette fjerner ekstra mellomrom

print(tekstFinal)