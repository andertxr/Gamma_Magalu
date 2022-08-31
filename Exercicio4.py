numero1 = float(input("Digite a primeira Nota:"))
numero2 = float(input("Digite a Segunda Nota:"))
numero3 = float(input("Digite a terceira Nota:"))
numero4 = float(input("Digite a Quarta Nota:"))

Media = float(numero1 + numero2 + numero3 + numero4)/4
print("A Media das Notas é:", Media)

if Media >= 6.0:
    print("Aluno Aprovado !! Parabéns")
else:
    print("Aluno Reprovado !! ")
