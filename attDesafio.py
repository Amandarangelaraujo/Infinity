tipo = str(input("qual tipo de combustível você deseja colocar? \n"))
litros = float(input("quantos litros voce deseja colocar? \n"))
if tipo == 'a' or tipo == 'A':
    if litros<=20:
         valor = (litros * 5.40)
         desconto = valor * (3/100)
    
    else:
        valor = (litros * 5.40)
        desconto = valor * (5/100)
    
else:
    if litros<=20:
       valor = (litros * 4.70)
       desconto = valor * (4/100)
    else:
       valor = (litros * 4.70)
       desconto = valor * (6/100)
total = valor - desconto
print("o valor é de: ")
print(total)



