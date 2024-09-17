# Les inn det desimale tallet som en heltall
desimal_tall = int(input("Skriv inn et desimalt tall: "))

if desimal_tall < 0:
    print("Vennligst skriv inn et positivt heltall.")
else:
    binary_str = ""
    
    if desimal_tall == 0:
        binary_str = "0"
    else:
        while desimal_tall > 0:
            rest = desimal_tall % 2
            binary_str = str(rest) + binary_str
            desimal_tall //= 2
    
    print(f"Binærtallet av det desimale tallet er {binary_str}.")
