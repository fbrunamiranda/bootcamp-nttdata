nome = "Bruna"
idade = 25
profissao = "Estudante"
linguagem = "Python"

# Old style % --> esta em desuso
# print("Olá, me chamo %s. Eu tenho %d anos de idade, sou %s e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))

# Método format (mesmo problema do primeiro caso)
# print("Olá, me chamo {}. Eu tenho {} anos de idade, sou {} e estou matriculada no curso de {}.".format(nome, idade, profissao, linguagem))

# print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, sou {profissao} e estou matriculada no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# f-string
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, sou {profissao} e estou matriculada no curso de {linguagem}.")

# Formatar strings com f-string

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")