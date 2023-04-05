import os
import requests
import shutil

pasta_atual = os.getcwd()  # Obtém o caminho da pasta atual
arquivos_originais = os.listdir(pasta_atual)  # Lista todos os arquivos da pasta atual

for arquivo_original in arquivos_originais:
    if arquivo_original.endswith('.txt'):  # Verifica se o arquivo é um arquivo de texto
        nome_arquivo, extensao = os.path.splitext(arquivo_original)
        nome_arquivo_saida = f'{nome_arquivo}-MAC-Vendors{extensao}'
        caminho_arquivo_saida = os.path.join(pasta_atual, nome_arquivo_saida)

        with open(arquivo_original) as arquivo_mac, open(caminho_arquivo_saida, 'w+') as arquivo_fabricantes:
            enderecos_mac = arquivo_mac.readlines()

            for endereco_mac in enderecos_mac:
                endereco_mac = endereco_mac.strip()
                url = f'https://api.macvendors.com/{endereco_mac}'
                resposta = requests.get(url)
                if resposta.status_code == 200:
                    fabricante = resposta.text
                else:
                    fabricante = f'Não encontrado: {endereco_mac}'

                arquivo_fabricantes.seek(0, 2)  # Posiciona o cursor no final do arquivo
                arquivo_fabricantes.write(f'{fabricante}\n')
                arquivo_fabricantes.flush()  # Salva as alterações no arquivo

                print(f'Endereço MAC {endereco_mac} processado. Fabricante: {fabricante}')

        shutil.copy2(arquivo_original, caminho_arquivo_saida)  # Faz a cópia do arquivo original com o nome modificado
