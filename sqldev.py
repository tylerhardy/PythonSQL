import sqlite3, os, csv, openpyxl, datetime
"""
1. Grab headers
2. Map headers to db columns
3. Check if key column has value
    if value - new dict > add key (asset_tag) value (WS0002131) to 

    else pass
"""
# Dictionary Map for PC Lifecycle .CSV files
excel_dict = {
    'D_CODE' : 'asset_tag',
    'D_TYPE' : 'type',
    'D_MAC_WIRED' : 'mac_wired',
    'D_MAC_WIRELESS' : 'mac_wireless',
    'D_AMT'	: 'cost',
    'D_ACQD_DATE' : 'purchase_date',
    'D_SERIAL_NUM' : 'serial_number',
    'D_PO' : 'po',
    'D_ORGN_CODE' : 'organization_code',
    'T_ORGN_CODE_DESC' : 'department',
    'D_LOCN_CODE_RESP' : 'location',
    'D_DESC' : 'description',
    'D_DEVICE_OWNER' : 'owner',
    'D_OS' : 'os',
}

"""Searches fo CSV files and create a list with its contents"""
# Create dict_list
dict_list = {}
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files
    name_var = os.path.splitext(csvFilename)[0]
    # print('Getting list of assets from [{0}]'.format(name_var))
    with open(csvFilename,'r') as csvFileObj:
        readerObj = csv.reader(csvFileObj)
        var_list = []
        hrow = next(readerObj)
        print(hrow)
        
        asset_id = hrow.index('D_CODE')
        type_id = hrow.index('D_TYPE')
        serial_id = hrow.index('D_SERIAL_NUM')
        location_id = hrow.index('D_LOCN_CODE_RESP')
        description_id = hrow.index('D_DESC')
        for row in readerObj:
            if row[type_id] == 'PC' or  row[type_id] == 'LT':
                var_list.append([row[asset_id]])
                dict_list[str(name_var)] = var_list
    csvFileObj.close()

for k, v in hrow:
    print(k)

def main():

if __name__ == '__main__':
    main()