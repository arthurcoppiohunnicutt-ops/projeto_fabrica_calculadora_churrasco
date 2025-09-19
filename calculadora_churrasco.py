# Crie um programa que calcule a quantidade de bebidas e de carne 
# para a organização de um churrasco
#
# Etapas da resolução
# 1) solicitar o numero de convidados
# 2) criar uma função para calcular a quantidade total de bebidas
# 3) criar uma função para calcular a quantidade total de carnes
# 4) apresentar o resultado com os valores de total de carne e bebidas 
# a serem comprados

convidados = int(input('Digite o numero de convidados:'))

def calcular_bebidas(convidados, consumo_por_pessoa_ml =800, volume_garrafa_litro =2.25):
    total_ml = convidados * consumo_por_pessoa_ml
    total_litro= total_ml/1000

    garrafas = int(total_litro//volume_garrafa_litro)
    if total_litro % volume_garrafa_litro >0:
        garrafas += 1
    return total_litro, garrafas

# resultado=calcular_bebidas(convidados)
# print(resultado)

def calcular_carne(convidados,consumo_por_pessoa_grama=400):
    total_gramas = convidados * consumo_por_pessoa_grama
    total_kg= total_gramas / 1000
    return total_kg

litros, garrafas = calcular_bebidas(convidados)
carne_kg= calcular_carne(convidados)

print('n__Quantidade total para Churrasco__')
print(f'Numero de connvidados: {convidados}.')
print(f'Refrigerantes necessarios: {litros:.2f} liros.')
print(f'Garrafas de 2,5L: {garrafas} unidades.')
print(f'Carne necessaria: {carne_kg:.2f} Kg')