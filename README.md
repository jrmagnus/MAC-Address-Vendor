# MAC Address to Vendor Script

This Python script takes a list of MAC addresses and exports them as a list of corresponding vendors.
Source Database:
https://maclookup.app/downloads/csv-database

## Requirements

- Python
- MAC addresses should be in the format `AA:BB:CC:00:11:22` (uppercase and colon-separated)

## Usage

1. **Input MAC Addresses:**
   - Place your list of MAC addresses in the `MacList` folder. Ensure the MAC addresses are in the format `AA:BB:CC:00:11:22`, with uppercase letters and colons.

2. **Run the Script:**
   - Execute the script `mac-vendor-local.py`.

3. **Output Vendor List:**
   - The vendor list will be exported to the `VendorList` folder.

## Example MAC Address Format

```plaintext
AA:BB:CC:00:11:22
