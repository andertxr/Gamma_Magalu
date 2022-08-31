cobertura_tinta = 3
capacidade_lata = 18
preco_lata = 80.0
tamanho_area = float(input("Digite o tamanho da área a ser pintada: (em m³)"))

litros = tamanho_area/cobertura_tinta
latas_inteiras = int(litros/capacidade_lata)
if (litros % capacidade_lata != 0):
    latas_inteiras += 1

valor_total = latas_inteiras * preco_lata

print("Quantidade de litros necessários:", litros)
print("Quantidade de latas necessárias:", latas_inteiras)
print("Valor total : R$", valor_total)
