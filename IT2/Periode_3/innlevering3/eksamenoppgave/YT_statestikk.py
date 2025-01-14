import pandas as pd  

def land():
    data = pd.read_csv("GlobalYouTubeStatistics.csv", # Relative path, fjern Innlevering_kap3/eksamenoppgave hvis du kjører fra eksamenoppgave
                    index_col = 0,          # Vi bruker kolonne 0 som indexen vår for dataen vår. Python teller fra 0 og oppover!
                    skiprows = (0),         # Det er vår interesse å hoppe over rad 0 fordi det er bare tekst, ikke "data"
                    sep = ",",              # Gir beskjed hva som sepererer dataen vår
                    na_values = ["nan"],    # Gir beskjed at "nan" er verdier som ikke har noe verdi, hindrer kluss!
                    encoding = "latin-1")   # Enkel måte å si hvilke bokstaver/tegn som brukes i CSV filen
    
    land = data["Country"].value_counts()   # Her definerer vi land med bruk av dataen ("Data") vi henter fra CSV filen, vi da tar fra kolonnen "Country" og teller antall land.
    top10land = land.head(10)               # Istedet å gi en hel liste over alle land, får vi en liste med top 10 land som har flest brukere på YT med land.head(10)

    print(f"Top 10 land med flest brukere på YouTube:\n{top10land}\n") # Printer informasjonen
    
   
land()

def gjennomsnitt():
    data = pd.read_csv("Innleverig_kap_3/eksamenoppgave/GlobalYouTubeStatistics.csv",
                        index_col = 0,
                        skiprows = (0),
                        sep = ",",
                        na_values = ["nan"],
                        encoding = "latin-1")

    antallland = {}              
    for i in range(data["Country"]):
        if data["Country"] in antallland:
            antallland[data["Country"]] += 1
        else:
            antallland[data["Country"]] = 1
            
    folgere = data["subscribers"]
    seere = data["video views"]

