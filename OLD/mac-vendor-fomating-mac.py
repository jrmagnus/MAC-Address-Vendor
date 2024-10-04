import os
import csv
import re

def normalize_mac_address(mac_address):
    # Remove todos os caracteres não hexadecimais (exceto letras e números)
    mac_address = re.sub(r'[^a-fA-F0-9]', '', mac_address)
    # Formatar o MAC para o formato 00:00:0C:DD:EE:FF
    formatted_mac = ':'.join(mac_address[i:i+2] for i in range(0, 12, 2))
    return formatted_mac.upper()

def search_manufacturer(mac_address):
    # Obter o caminho completo do arquivo CSV de fabricantes
    current_folder = os.getcwd()
    csv_file_path = os.path.join(current_folder, 'mac-vendors-export.csv')

    # Pesquisar no arquivo CSV
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for row in csv_reader:
            if mac_address.startswith(row[0]):
                return row[1]
    return 'Not found'

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

        # Buscar fabricantes para cada endereço MAC na lista
        with open(mac_file_path, 'r') as mac_file:
            for mac_address in mac_file:
                normalized_mac = normalize_mac_address(mac_address.strip())
                manufacturer = search_manufacturer(normalized_mac)
                print(f'{output_filename} Processing MAC Address: {normalized_mac} from {manufacturer}')
                message = f'{normalized_mac} - {manufacturer}\n'
                output_file.write(message)

    print(f'File {output_filename} successfully created in the {vendor_list_folder} folder')
