# lista_de_compras = ["ovos" , "farinha", "leite"  , "confete","arroz"]

# for item in lista_de_compras:
#     print(f"comprei o item: {item}")


numero = 0 
while True :

    numero += 1 
    if numero == 100:
        break
    if numero % 2 == 0:
        print(f"O NUMERO : {numero} é par  ")
        continue

    print(f"o numero: {numero} é impar ")
