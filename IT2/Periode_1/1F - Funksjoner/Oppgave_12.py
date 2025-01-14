"""
grunn = int(input("Grunnlinje: "))
hoyde = int(input("Høyde: "))

def arealtrekant():
    return (grunn * hoyde)/2

print(f"{arealtrekant()}")
"""

"""
def arealtrekant(grunn, hoyde):
    return (grunn * hoyde)/2

print(arealtrekant(4,10))
"""

def arealtrekant(grunn, hoyde):
    return (grunn * hoyde)/2

grunn = int(input("Grunnlinje: "))
hoyde = int(input("Høyde: "))

print(arealtrekant(grunn, hoyde))