## English

import os
import csv

def search_manufacturer(mac_address):
    # Get the full path of the manufacturer CSV file
    current_folder = os.getcwd()
    csv_file_path = os.path.join(current_folder, 'mac-vendors-export.csv')

    # Search in the CSV file
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for row in csv_reader:
            if mac_address.startswith(row[0]):
                return row[1]
    return 'Not found'

mac_list_folder = 'Mac list'
vendor_list_folder = 'Vendor list'

# Create the Vendor list folder if it doesn't exist
if not os.path.exists(vendor_list_folder):
    os.makedirs(vendor_list_folder)

# Iterate through each file in the Mac list folder
all_files_processed = False
for filename in os.listdir(mac_list_folder):
    mac_file_path = os.path.join(mac_list_folder, filename)

    # Create a new file for each MAC address list
    output_filename = os.path.splitext(filename)[0] + '_manufacturers.txt'
    output_file_path = os.path.join(vendor_list_folder, output_filename)
    with open(output_file_path, 'w') as output_file:

        # Search for manufacturers for each MAC address in the list
        with open(mac_file_path, 'r') as mac_file:
            for mac_address in mac_file:
                manufacturer = search_manufacturer(mac_address.strip())
                print(f'{output_filename} Processing MAC Address: {mac_address.strip()} from {manufacturer}')
                message = f'{manufacturer}\n'
                output_file.write(message)

    print(f'File {output_filename} successfully created in the {vendor_list_folder} folder')

    # Check if this was the last file in the Mac list folder
    if filename == os.listdir(mac_list_folder)[-1]:
        all_files_processed = True

    # Exit the loop if all files have been processed
    if all_files_processed:
        break