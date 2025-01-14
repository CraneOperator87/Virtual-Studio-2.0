navn = ["Anne", "Per", "Ole", "Anne", "Lise", "Ole", "Anne", "Per", "Anne", "Tor", "Ole"]

while "Anne" in navn:
    fjernindeks_anne = navn.index("Anne")
    navn.pop(fjernindeks_anne)

navn.insert(0,"Anne")

while "Per" in navn: 
    fjernindeks_per = navn.index("Per")
    navn.pop(fjernindeks_per)

navn.insert(1, "Per")

while "Ole" in navn: 
    fjernindeks_ole = navn.index("Ole")
    navn.pop(fjernindeks_ole)

navn.insert(2, "Ole")

print(navn)


