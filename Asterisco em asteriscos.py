# Tamanho do asterisco
tamanho = 25  # Deve ser um número ímpar para garantir um centro

# Verifica se o tamanho é ímpar
if tamanho % 2 == 0:
    print("Por favor, insira um tamanho ímpar.")
else:
    # Índice do centro
    centro = tamanho // 2

    for i in range(tamanho):
        linha = ""
        for j in range(tamanho):
            # Desenha a linha horizontal, vertical ou diagonais
            if i == centro or j == centro or i == j or i + j == tamanho - 1:
                linha += "*"
            else:
                linha += " "
        print(linha)
input()