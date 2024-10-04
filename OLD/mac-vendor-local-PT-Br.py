## PT-BR
    
import os
import csv

def pesquisar_fabricante(endereco_mac):
    # Obtém o caminho completo do arquivo CSV de fabricantes
    pasta_atual = os.getcwd()
    caminho_arquivo_csv = os.path.join(pasta_atual, 'mac-vendors-export.csv')

    # Faz a pesquisa no arquivo CSV
    with open(caminho_arquivo_csv, newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=',', quotechar='"')
        for linha in leitor_csv:
            if endereco_mac.startswith(linha[0]):
                return linha[1]
    return 'Não encontrado'

pasta_mac_list = 'Mac list'
pasta_vendor_list = 'Vendor list'

# Cria a pasta Vendor list se ela não existir
if not os.path.exists(pasta_vendor_list):
    os.makedirs(pasta_vendor_list)

# Percorre cada arquivo na pasta Mac list
todos_arquivos_processados = False
for nome_arquivo in os.listdir(pasta_mac_list):
    caminho_arquivo_mac = os.path.join(pasta_mac_list, nome_arquivo)

    # Cria um novo arquivo para cada lista de endereços MAC
    nome_arquivo_saida = os.path.splitext(nome_arquivo)[0] + '_fabricantes.txt'
    caminho_arquivo_saida = os.path.join(pasta_vendor_list, nome_arquivo_saida)
    with open(caminho_arquivo_saida, 'w') as arquivo_saida:

        # Faz a pesquisa de fabricantes para cada endereço MAC na lista
        with open(caminho_arquivo_mac, 'r') as arquivo_mac:
            for endereco_mac in arquivo_mac:
                fabricante = pesquisar_fabricante(endereco_mac.strip())
                print(f'{nome_arquivo_saida} Processando endereço MAC: {endereco_mac.strip()} de {fabricante}')
                mensagem = f'{fabricante}\n'
                arquivo_saida.write(mensagem)

    print(f'Arquivo {nome_arquivo_saida} criado com sucesso na pasta {pasta_vendor_list}')

    # Verifica se este foi o último arquivo na pasta Mac list
    if nome_arquivo == os.listdir(pasta_mac_list)[-1]:
        todos_arquivos_processados = True

    # Sai do loop se todos os arquivos foram processados
    if todos_arquivos_processados:
        break
