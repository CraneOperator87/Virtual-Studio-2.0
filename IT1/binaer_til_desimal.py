binary_str = input("Skriv inn et binært tall: ")

decimal_value = 0
length = len(binary_str)
    
for i in range(length):
    bit = int(binary_str[i])
    decimal_value += bit * (2 ** (length - i - 1))
    
print(f"Desimalverdien av binærtall {binary_str} er {decimal_value}.")
