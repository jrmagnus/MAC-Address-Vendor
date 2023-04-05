import os

# Obtém o caminho da pasta onde o script está sendo executado
caminho_pasta = os.getcwd()

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir(caminho_pasta):
    # Verifica se o arquivo é um arquivo de texto
    if nome_arquivo.endswith('.txt'):
        # Abre o arquivo original
        with open(nome_arquivo, 'r') as arquivo_origem:
            # Cria um novo nome para o arquivo filtrado
            nome_arquivo_filtrado = nome_arquivo.replace('.txt', '_filtrado.txt')
            # Cria um novo arquivo para armazenar as informações filtradas
            with open(nome_arquivo_filtrado, 'w') as arquivo_filtrado:
                # Lê o arquivo de origem linha por linha
                for linha in arquivo_origem:
                    # Verifica se a linha contém a informação de last-caller-id=
                    if 'last-caller-id=' in linha:
                        # Extrai o valor de last-caller-id=
                        last_caller_id = linha.split('last-caller-id=')[1].split()[0]
                        # Escreve a informação filtrada no arquivo de destino
                        arquivo_filtrado.write(f'{last_caller_id}\n')