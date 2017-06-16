import sqlite3, os, csv, openpyxl, datetime
"""
1. Grab headers
2. Map headers to db columns
3. Check if key column has value
    if value - new dict > add key (asset_tag) value (WS0002131) to 

    else pass
"""
def BuildDatabase():
    """Build the inventoyr database"""
    # Database name
    sqlite_file = 'cos_inventory_db.sqlite'

    # Table Variables
    table_name1 = 'hardware_inventory'

    # Columns for asset_tags table
    new_field = 'my_1st_column'

    # column data type for asset_tags table
    field_type = 'INTEGER'  # column data type

    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    # Creating a new SQLite table with 1 column
    c.execute('CREATE TABLE {tn} ({nf} {ft})'.format(tn=table_name1, nf=new_field, ft=field_type))

    # Creating a second table with 1 column and set it as PRIMARY KEY
    # note that PRIMARY KEY column must consist of unique values!
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=table_name2, nf=new_field, ft=field_type))

    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()


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