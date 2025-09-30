num = int(input("Digite um número: "))

if num < 0:
    print("Fatorial não é definido para números negativos.")
else:
    fat = 1
    for i in range(1, num + 1):
        fat *= i
    print(f"O fatorial de {num} é {fat}")
