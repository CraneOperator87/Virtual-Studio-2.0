navn = "Pål"
karakterer = [3, 4, 6, 6, 5, 4]

karaktertekst = ""
for i in range(len(karakterer)):
  karaktertekst += str(karakterer[i])

print(f"{navn} fikk karakterene {karaktertekst}")