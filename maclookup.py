import pandas as pd

# 1) Load your MAC list (plain hex, no separators) from macaddress.csv
df = pd.read_csv('macaddress.csv', header=None, names=['mac'], dtype=str)
df['mac'] = df['mac'].str.strip().str.upper()

# 2) Extract the OUI (first 6 hex digits) and format as XX:XX:XX
df['OUI'] = df['mac'].str[:6].apply(lambda x: ':'.join([x[i:i+2] for i in range(0, 6, 2)]))

# 3) Read the local IEEE OUI dump (saved as oui.txt in the same folder)
lookup = {}
with open('oui.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if '(hex)' in line:
            parts = line.split()
            # parts[0] is like "XX-XX-XX", parts[2:] is the vendor name
            oui = parts[0].replace('-', ':').upper()
            vendor = ' '.join(parts[2:])
            lookup[oui] = vendor

# 4) Map each OUI to its vendor (or "not found")
df['Manufacturer'] = df['OUI'].map(lookup).fillna('not found')

# 5) Write out the result
df[['mac', 'Manufacturer']].to_csv('mac_with_manufacturer.csv', index=False)

print("✅ Done! See mac_with_manufacturer.csv")
