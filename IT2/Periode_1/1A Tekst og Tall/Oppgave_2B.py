tall = int(input("Skriv inn et tall: "))


def sjekk_siffer(tall): 
    if 0 <= tall < 10:
        return "ensifferet tall (0-9)"
    elif 10 <= tall < 100:
        return "tosifferet tall (10-99)"
    elif 100 <= tall < 1000:
        return "tresifferet tall (100-999)"
    elif 1000 <= tall < 10000:
        return "firesifferet tall (1000-9999)"
    else:
        return "Mer en et firesifferet tall (10000+)"

resultat = sjekk_siffer(tall)   
print(f"Tallet er et {resultat}")



