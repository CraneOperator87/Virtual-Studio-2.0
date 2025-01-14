byer = ["OSLOO", "Trondheim", "Bergen", "Stavaangir", "Kristiansand", "Drammen", "Tromsø"]


m = byer.index("Stavaangir") # Vi finner verdien til "OSLOO" og "Stavaangir", og definerer det som "n" og "m"
n = byer.index("OSLOO")  

byer.pop(n)     
byer.pop(m)           

byer.insert(n,"Oslo")
byer.insert(m, "Stavanger")

print(byer)