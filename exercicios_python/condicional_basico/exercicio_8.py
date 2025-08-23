# 8. Solicite ao usuário duas notas e informe se ele foi aprovado (média maior ou igual a 6) ou reprovado.

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2

print("A média das notas é %.1f"%(media))

if media > 6:
    print("Aprovado")
else:
    print("Reprovado")