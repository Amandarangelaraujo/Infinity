media = 0
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))

media=(nota1+nota2)/2

if media==10:
    print("voce foi aprovado! com DEZ, parabéns")
elif media<7:
    print("você foi reprovado")
else:
    print("voce foi aprovado")
