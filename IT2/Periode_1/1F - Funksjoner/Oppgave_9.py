def navnskilt(navn):
    print("+-", end="")
    for lengde in navn:
        print(f"-", end="")
    print("-+", end="")
    print(f"\n| {navn} |")
    print("+-", end="")
    for lengde in navn:
        print("-", end="")
    print("-+", end="")


namn = input("Skriv inn navnet ditt: ")
navnskilt(namn)





