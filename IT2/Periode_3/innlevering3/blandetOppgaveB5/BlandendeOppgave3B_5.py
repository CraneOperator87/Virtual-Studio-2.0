"""
Lag et program som leser inn fila.
Skriv ut en oversiktlig liste over alle oppgavene, én oppgave per rad.
Skriv ut en liste over alle oppgavene som ikke er utført (de er ikke completed ), og en liste over alle oppgavene som er utført.
Finn ut hvilken bruker som har utført flest oppgaver. Hvor mange oppgaver har hen utført?
Finn ut hvilken bruker som har utført færrest oppgaver. Hvor mange oppgaver har hen utført?
"""

import json
# HUSK Å BYTT FIL!!!!!!!!!
fil = "./Periode3/Innleveirng_kap_3/blandetOppgaveB5/todos.json"

class Oppgave:
    def __init__(self, bruker: int, nr: int, navn: str, ferdig: bool):
        self.bruker = bruker
        self.nr = nr
        self.navn = navn
        self.ferdig = ferdig

class OppgaveBehandler:
    def __init__(self, filnavn: str):
        self.filnavn = filnavn
        self.oppgaverFerdig = []
        self.oppgaverIkkeFerdig = []
        self.bruker = {}

    def lesFraFil(self):
        with open(self.filnavn, "r") as f:
            data = json.load(f)
            for oppgave in data:
                if oppgave["completed"] == True:
                    self.oppgaverFerdig.append(Oppgave(oppgave["userId"], oppgave["id"], oppgave["title"], oppgave["completed"]))
                else:
                    self.oppgaverIkkeFerdig.append(Oppgave(oppgave["userId"], oppgave["id"], oppgave["title"], oppgave["completed"]))

    def lagBrukerListe(self):
        for oppgave in self.oppgaverFerdig:
            if oppgave.bruker in self.bruker:
                self.bruker[oppgave.bruker] += 1
            else:
                self.bruker[oppgave.bruker] = 1

    def skrivUtOppgaver(self):
        for oppgave in self.oppgaverFerdig:
            print(f"Oppgave {oppgave.nr} er utført av bruker: {oppgave.bruker} og oppgaven heter: {oppgave.navn}")
        for oppgave in self.oppgaverIkkeFerdig:
            print(f"Oppgave {oppgave.nr} er ikke utført av bruker: {oppgave.bruker} og oppgaven heter: {oppgave.navn}")

    def brukerMedFlestOppgaver(self):
        max_bruker = max(self.bruker, key=self.bruker.get)
        return max_bruker, self.bruker[max_bruker]

    def brukerMedFærrestOppgaver(self):
        min_bruker = min(self.bruker, key=self.bruker.get)
        return min_bruker, self.bruker[min_bruker]
    
def main():
    oppgave_behandler = OppgaveBehandler(fil)
    oppgave_behandler.lesFraFil()
    oppgave_behandler.lagBrukerListe()
    oppgave_behandler.skrivUtOppgaver()

    max_bruker, max_oppgaver = oppgave_behandler.brukerMedFlestOppgaver()
    print(f"Bruker: {max_bruker}, har utført flest oppgaver med {max_oppgaver} ferdige oppgaver!")

    min_bruker, min_oppgaver = oppgave_behandler.brukerMedFærrestOppgaver()
    print(f"Bruker: {min_bruker}, har utført minst oppgaver med {min_oppgaver} uferdige oppgaver!.")


main()