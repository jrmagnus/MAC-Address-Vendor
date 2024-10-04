import os
import csv
import re
import requests

def download_csv():
    # URL base para o download (modifique conforme necessário)
    base_url = 'https://maclookup.app/downloads/csv-database/get-db'
    # Pasta para salvar o arquivo CSV baixado
    current_folder = os.getcwd()
    csv_file_path = os.path.join(current_folder, 'mac-vendors-export.csv')

    # Baixar o arquivo
    print("Baixando arquivo CSV de fabricantes...")
    response = requests.get(base_url, allow_redirects=True)

    if response.status_code == 200:
        with open(csv_file_path, 'wb') as file:
            file.write(response.content)
        print(f'Arquivo CSV baixado com sucesso: {csv_file_path}')
    else:
        print('Erro ao baixar o arquivo CSV.')
    
    return csv_file_path

def normalize_mac_address(mac_address):
    # Remove todos os caracteres não hexadecimais (exceto letras e números)
    mac_address = re.sub(r'[^a-fA-F0-9]', '', mac_address)
    # Formatar o MAC para o formato 00:00:0C:DD:EE:FF
    formatted_mac = ':'.join(mac_address[i:i+2] for i in range(0, 12, 2))
    return formatted_mac.upper()

def load_manufacturer_data(csv_file_path):
    # Carregar os dados de fabricantes na memória como um dicionário
    manufacturer_dict = {}

    # Ler o arquivo CSV e armazenar no dicionário
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for row in csv_reader:
            if len(row) >= 2:  # Verificar se há dados suficientes
                prefix = row[0].upper()
                manufacturer = row[1]
                manufacturer_dict[prefix] = manufacturer
    return manufacturer_dict

def search_manufacturer(mac_address, manufacturer_dict):
    # Buscar no dicionário pré-carregado os três primeiros octetos do MAC
    mac_prefix = mac_address[:8]  # Considera os primeiros 6 caracteres (3 pares hexadecimais)
    return manufacturer_dict.get(mac_prefix, 'Not found')

# Baixar o arquivo CSV mais recente
csv_file_path = download_csv()

# Carregar os dados de fabricantes uma vez
manufacturer_data = load_manufacturer_data(csv_file_path)

mac_list_folder = 'Mac list'
vendor_list_folder = 'Vendor list'

# Criar a pasta Vendor list se não existir
if not os.path.exists(vendor_list_folder):
    os.makedirs(vendor_list_folder)

# Iterar por cada arquivo na pasta Mac list
for filename in os.listdir(mac_list_folder):
    mac_file_path = os.path.join(mac_list_folder, filename)

    # Criar um novo arquivo para cada lista de endereços MAC
    output_filename = os.path.splitext(filename)[0] + '_manufacturers.txt'
    output_file_path = os.path.join(vendor_list_folder, output_filename)
    
    with open(output_file_path, 'w') as output_file:
        buffer = []
        
        # Buscar fabricantes para cada endereço MAC na lista
        with open(mac_file_path, 'r') as mac_file:
            for mac_address in mac_file:
                normalized_mac = normalize_mac_address(mac_address.strip())
                manufacturer = search_manufacturer(normalized_mac, manufacturer_data)
                print(f'{output_filename} Processing MAC Address: {normalized_mac} from {manufacturer}')
                buffer.append(f'{normalized_mac} - {manufacturer}\n')
        
        # Escrever os resultados em bloco
        output_file.writelines(buffer)

    print(f'File {output_filename} successfully created in the {vendor_list_folder} folder')
