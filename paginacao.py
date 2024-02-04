# Tamanho da página em bytes
tamanho_pagina = 4096  # 4 KB

# Número de páginas na memória física
num_paginas_memoria = 8

# Tabela de páginas (Page Table) simulada
tabela_paginas = [None] * num_paginas_memoria

# Preenchendo a tabela de páginas com endereços físicos simulados
for i in range(num_paginas_memoria):
    tabela_paginas[i] = i * tamanho_pagina

# Função para simular a busca de endereço
def buscar_endereco(endereco_virtual):
    numero_pagina = endereco_virtual // tamanho_pagina
    deslocamento = endereco_virtual % tamanho_pagina

    if numero_pagina < 0 or numero_pagina >= num_paginas_memoria:
        return None, "Erro: Página não encontrada"

    if tabela_paginas[numero_pagina] is None:
        # Simulação de falha de página: recarrega a página na memória
        tabela_paginas[numero_pagina] = numero_pagina * tamanho_pagina
        print("Página", numero_pagina, "recarregada na memória.")

    endereco_fisico = tabela_paginas[numero_pagina] + deslocamento
    return endereco_fisico, None

# Simulação de busca de endereço
enderecos_virtuais = [10000, 8192, 4096, 16384]  # Endereços virtuais a serem buscados

for endereco_virtual in enderecos_virtuais:
    endereco_fisico, erro = buscar_endereco(endereco_virtual)

    if erro:
        print(erro)
    else:
        print("Endereço virtual:", endereco_virtual)
        print("Endereço físico correspondente:", endereco_fisico)
