import json
import matplotlib.pyplot as plt

fil = "./Periode3/Innlevering_kap_3/Periode3_JSON/todos_oppgave1.json"

def main():
    with open(fil, "r") as file: # Åpner filen og leser den.
        data = json.load(file)

    antall_brukere = 0
    fullførte = 0
    ikke_fullførte = 0

    utførte = []
    ikke_utførte = []

    beste = {}

    for oppgave in data:
        # Teller antall brukere:
        if oppgave["userId"] > antall_brukere:
            antall_brukere += 1
        # Teller antall fullførte oppgaver:
        if oppgave["completed"] == True:
            fullførte += 1
            utførte.append(oppgave)
        # Finner ut den beste brukeren:
            oppgave["userId"] = int(oppgave["userId"])
            if oppgave["userId"] in beste:
                beste[oppgave["userId"]] += 1
            else:
                beste[oppgave["userId"]] = 1
        # Teller antall ikke fullførte oppgaver:
        else:
            ikke_fullførte += 1
            ikke_utførte.append(oppgave)
        
        if not oppgave["estimat"]:
            oppgave["estimat"] = "1d"

    # Fullførte Oppgaver:
    print(f"\nListen over fullførte oppgaver i prosjektet:\n")
    for oppgave in utførte:
        print(f"[{oppgave["id"]}]: {oppgave["title"]}, Ansvarlig bruker: {oppgave["userId"]}, Tid brukt = {oppgave["estimat"]}")
    # Ikke fullførte Oppgaver:
    print(f"\nListen over uførte oppgaver i prosjektet: \n")
    for oppgave in ikke_utførte:
        print(f"[{oppgave["id"]}]: {oppgave["title"]}, Ansvarlig bruker: {oppgave["userId"]}, Tid brukt = {oppgave["estimat"]}")

    print(f"\nAntall brukere på dette prosjektet: {antall_brukere} brukere.")
    print(f"Antall fullførte oppgaver: {fullførte} oppgaver.")
    print(f"Antall oppgaver som ikke er fullført: {ikke_fullførte} opgpaver.\n")
    print(f"Brukeren med flest fullførte oppgaver er bruker: {max(beste, key=beste.get)} med {max(beste.values())} fullførte oppgaver.")
    print(f"Brukeren med færrest fullførte oppgaver er bruker: {min(beste, key=beste.get)} med {min(beste.values())} fullførte oppgaver.")

def graf():
    with open(fil, 'r') as file: # Les av fil
        data = json.load(file)
    
    ferdige = []
    ikke_ferdige = []
    # Leser hvilken oppgaver er ferdige og ikke ferdige
    for oppgave in data:
        if oppgave["completed"] == True:
            ferdige.append(oppgave) 
        else:
            ikke_ferdige.append(oppgave)

    # Plotter grafen: len(ferdige) = Lengden til Ferdige listen, len(ikke_ferdige) = Lengden til Ikke Ferdige listen
    # Labels = Navn til hver sektor
    # labeldistance = Avstand mellom labels og sektorer
    # wedgeprops = Avnsert koding som gir hvite mellomrom mellom sektorene
    plt.pie([len(ferdige), len(ikke_ferdige)], labels=["Ferdige", "Ikke Ferdige"], labeldistance=1.15, wedgeprops = { "linewidth": 1, "edgecolor": "white" } )
    plt.show()

def prosentvis_graf():
    with open(fil, 'r') as file:
        data = json.load(file)
    
    ferdige = []
    ikke_ferdige = []
    beste = {}
    for oppgave in data:
        if oppgave["completed"] == True:
            ferdige.append(oppgave) 
            oppgave["userId"] = int(oppgave["userId"])
            if oppgave["userId"] in beste:
                beste[oppgave["userId"]] += 1
            else:
                beste[oppgave["userId"]] = 1
        else:
            ikke_ferdige.append(oppgave)

    # Copilot:
    totalt = len(ferdige)
    prosent = [(user, tasks / totalt * 100) for user, tasks in beste.items()]
    users, percentages = zip(*prosent)
    plt.pie(percentages, labels=users, autopct='%1.1f%%', labeldistance=1.15, wedgeprops = { "linewidth": 1, "edgecolor": "white" } )
    plt.title("Prosentvis graf over brukere som har fullført oppgaver")
    plt.show()


main()
graf()
prosentvis_graf()



