class Game:
    def __init__(self):
        self.characters = {
            "1": {"name": "Character1", "difficulty": "Easy", "method": self.karaktervalg_easy},
            "2": {"name": "Character2", "difficulty": "Medium", "method": self.karaktervalg_medium},
            "3": {"name": "Character3", "difficulty": "Hard", "method": self.karaktervalg_hard}
        } 
        self.is_running = False

    def introduksjon(self):
        print("Velkommen til historiske spillet laget av Hassan, Fatlinda og Kajus :D")
        print("I dette spillet vil du få muligheter til å utforske svartedauden perioden,")
        print("og du vil ha mulighet til å oppleve hvordan det var å leve i ved forskjellige vanskelighetsgrader.")
        bruker_valg = input("Er du klar til å starte spillet? (ja/nei): ")
        if bruker_valg.lower() == "ja":
            print("La oss starte spillet!")
            self.start_spill()
        else:
            print("Ok, vi venter til du er klar.")
            return

    def karaktervalg_easy(self):
        print("Du har valgt vanskelighetsgraden Easy.")
        print("\nKarakteren din er rik handelsmann fra Frankrike.")
        print("Du har en middels stor familie (på den tiden), og har en kone og 3 barn.")
        print("Dere er kristne, og har en stor gård med få dyr.")
        print("Dere har et gård der det er mest avlinger, og er ommringet av skog.")
        print("Gården har god tilgang til vann, og gården er selvforsynt med mat.")
        print("Lykke til!")
        print("")
    
    def karaktervalg_medium(self):
        print("Du har valgt vanskelighetsgraden Medium.")
        print("\nKarakteren din er en rik bonde fra Norge.")
        print("Du har en liten familie (på den tiden), og har en kone og 2 barn.")
        print("Dere er kristne, og har en liten gård med få dyr.")
        print("Dere har et lite hus, og dere jobber på felles gården,")
        print("der det er litt avlinger, og er ommringet av skog.")
        print("Gården har god tilgang til vann, men huset har ikke vann eller mat")
        print("Det er en utfordning å skaffe seg vann")
        print("Lykke til!")
        print("")
    
    def karaktervalg_hard(self):
        print("Du har valgt vanskelighetsgraden Hard.")
        print("\nKarakteren din er en serf fra Tyskland.")
        print("Du har bare en kone og har så vidt rå til hus.")
        print("Du jobber for adelen i storbyen, der jobben din er å vaske klær.")
        print("Du og konen din er ikke religiøse, og dere har ingen annet valg enn å jobbe for adelen.")
        print("Adelen betaler dere med mat og drikke, for den harde jobben dere gjør.")
        print("Det er veldig utfordrende å skaffe seg mat og drikke, og å flytte fra byen er ikke realistisk")
        print("Dessuten har kirken bannlyst dere, og dere har ingen sammfunsstøtte.")
        print("Lykke til!")
        print("")

    def karaktervalg(self):
        print("Velg karakteren din:")
        for i, character in enumerate(self.characters.keys()):
            print(f"{i+1}. {self.characters[character]['name']} - {self.characters[character]['difficulty']}")
        choice = int(input("Skriv inn valget ditt: ")) - 1
        if choice in range(len(self.characters)):
            self.selected_character = list(self.characters.keys())[choice]
            print(f"Du har valgt: {self.characters[self.selected_character]['name']} med vanskelighetsgraden {self.characters[self.selected_character]['difficulty']}")
            self.characters[self.selected_character]['method']()  # Call the method associated with the selected character
        else:
            print("Invalid choice. Please try again.")
            self.karaktervalg()

    def start_spill(self):
        self.is_running = True
        print(f"\nSpillet har startet.\n")
        self.karaktervalg()

    def run(self):
        self.introduksjon()

game = Game()
game.run()