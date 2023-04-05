import csv
import os

# criar uma lista para armazenar as tabelas de todos os arquivos
tabelas = []

# percorrer todos os arquivos da pasta "Originals"
for nome_arquivo in os.listdir('Originals'):
    caminho_arquivo = os.path.join('Originals', nome_arquivo)
    
    # abrir o arquivo de texto
    with open(caminho_arquivo, 'r') as arquivo_txt:
        tabela = []
        for linha in arquivo_txt:
            if 'name=' in linha and 'profile=' in linha and 'last-caller-id=' in linha:
                nome = linha.split('name=')[1].split()[0]
                plano = linha.split('profile=')[1].split()[0]
                aparelho = linha.split('last-caller-id=')[1].split()[0]
                tabela.append([nome, plano, aparelho])

    # ler o arquivo CSV com as informações dos fabricantes
    with open('mac-vendors-export.csv', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=',')
        fabricantes = {}
        for linha in leitor_csv:
            mac_prefixo = linha[0].replace(':', '').upper()
            fabricante = linha[1]
            fabricantes[mac_prefixo] = fabricante

    # substituir o MAC Address na coluna 3 da tabela exportada pelo nome do fabricante encontrado
    for linha in tabela:
        mac_prefixo = linha[2].replace(':', '')[:6].upper()
        if mac_prefixo in fabricantes:
            linha[2] = fabricantes[mac_prefixo]
    
    # adicionar a tabela à lista de tabelas
    tabelas.append(tabela)

# exportar a lista de tabelas como um novo arquivo csv
with open('tabela_exportada.csv', 'w', newline='') as arquivo_exportado:
    escritor_csv = csv.writer(arquivo_exportado, delimiter=',')
    escritor_csv.writerow(['Arquivo', 'Coluna 1', 'Coluna 3', 'Coluna 2'])  # escrever o cabeçalho da tabela
    for i, tabela in enumerate(tabelas):
        for linha in tabela:
            escritor_csv.writerow([os.path.splitext(os.listdir('Originals')[i])[0], linha[0], linha[2], linha[1]])  # escrever as linhas da tabela, trocando a coluna 3 pelo fabricante
