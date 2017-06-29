import os, csv, datetime
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


def check_serial_number(conn, table, insert, values):
    serial_index = (insert.index('serial_number'))
    serial_value = values[serial_index]
    query = "SELECT id, serial_number FROM {0} WHERE serial_number='{1}';".format(table, serial_value)
    # print(query)
    cur = conn.cursor()
    cur.execute(query)
    serial_row = cur.fetchone()
    if serial_row is None:
        return _get_or_insert(conn, table, insert, values, -1)
    else:
        print('Property [{0}] already exists with [ID:{1}]'.format(serial_value, serial_row[0]))
        return serial_row[0]


def check_asset_id(conn, table, insert, values, id):
    asset_index = (insert.index('asset_tag'))
    asset_value = values[asset_index]
    insert.append('properties_id')
    values.append(str(id))
    query = "SELECT id, asset_tag FROM {0} WHERE asset_tag='{1}';".format(table, asset_value)
    # print(query)
    cur = conn.cursor()
    cur.execute(query)
    asset_row = cur.fetchone()
    if asset_row is None:
        return _get_or_insert(conn, table, insert, values, id)
    else:
        print('Asset [{0}] already exists with [ID:{1}]'.format(asset_value, asset_row[0]))
        return asset_row[0]


def _get_or_insert(conn, table, insert, values, id):
    # get_query = 'SELECT {0} FROM {1}'.format()
    insert = ', '.join(insert)
    values = "\"" + "\",\"".join(values) + "\""
    query_string = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(table,insert,values)
    print('Executing [{0}]'.format(query_string))
    # print(query_string)
    cur = conn.cursor()
    cur.execute(query_string)
    return cur.lastrowid


def main():
    # Global variables
    database = "cos_inventory.db"
    TABLE_PROPERTIES = 'properties'
    TABLE_ASSETS = 'assets'

    # Establish the database connection
    conn = create_connection(database)

    # With connection open
    with conn:

        # Dictionary map of the PC Lifecycle .csv files to SQL table and columns
        pcl_excel_dict = {
            'D_TYPE' : [TABLE_PROPERTIES, 'type'],
            'D_MAC_WIRED' : [TABLE_PROPERTIES, 'mac_wired'],
            'D_MAC_WIRELESS' : [TABLE_PROPERTIES, 'mac_wireless'],
            'D_SERIAL_NUM' : [TABLE_PROPERTIES, 'serial_number'],
            'D_DESC' : [TABLE_PROPERTIES, 'description'],
            'D_CODE' : [TABLE_ASSETS, 'asset_tag'],
            'D_AMT'	: [TABLE_ASSETS, 'cost'],
            'D_ACQD_DATE' : [TABLE_ASSETS, 'purchase_date'],
            'D_PO' : [TABLE_ASSETS, 'po'],
            'D_ORGN_CODE' : [TABLE_ASSETS, 'organization_code'],
            'T_ORGN_CODE_DESC' : [TABLE_ASSETS, 'department'],
            'D_LOCN_CODE_RESP' : [TABLE_ASSETS, 'location'],
            'D_DEVICE_OWNER' : [TABLE_ASSETS, 'owner']
        }

        # Read all .csv files in folder. 
        for csvFilename in os.listdir('.'):
            # Looks at every file in folder, if not .csv then skip to next file.
            if not csvFilename.endswith('.csv'):
                continue

            # Opens the .csv file in read only format
            with open(csvFilename,'r') as csvFileObj:
                print('\nReading [{0}]...'.format(csvFilename))

                # Pulls in contents of .csv file into an excel file object
                _EXCEL_FILE_OBJECT = csv.reader(csvFileObj)

                # Pulls the headers out of the excel file object
                EXCEL_TOP_ROW = next(_EXCEL_FILE_OBJECT)

                # Declare empty properties list
                PROPERTIES_LIST = []

                row_count = 0
                # Loops through each row in the excel file object
                for data_row in _EXCEL_FILE_OBJECT:
                    row_count += 1
                    print('\nInserting data from row [{0}] into [{1}] from [{2}]'.format(row_count, database, csvFilename))
                    # Declare dictionary with keys as the SQL tables and values as empty lists
                    SQL_DICT = {TABLE_PROPERTIES:[], TABLE_ASSETS:[]}

                    # Loops through each 'cell' of the row, pulls out the index of the 'cell' and the value of the 'cell' through enumeration of each row
                    for index, item in enumerate(data_row):
                        SQL_IDENTIFIER = pcl_excel_dict.get(EXCEL_TOP_ROW[index])
                        if SQL_IDENTIFIER is not None:
                            if str(item).lower().strip() is not "":
                                if SQL_IDENTIFIER[0] == TABLE_ASSETS:
                                    SQL_DICT[TABLE_ASSETS].append([item, SQL_IDENTIFIER[1]])
                                elif SQL_IDENTIFIER[0] == TABLE_PROPERTIES:
                                    SQL_DICT[TABLE_PROPERTIES].append([item, SQL_IDENTIFIER[1]])
                    _ASSET_TAG_ID = ""
                    asset_sql_insert = []
                    assets_sql_values = []
                    properties_sql_insert = []
                    properties_sql_values = []
                    property_id = -1
                    table_list = []
                    for table, columns in SQL_DICT.items():
                        table_list.append(table)
                        for column in columns:
                            if table == TABLE_PROPERTIES:
                                properties_sql_insert.append(column[1])
                                properties_sql_values.append(column[0])
                            elif table == TABLE_ASSETS:
                                asset_sql_insert.append(column[1])
                                assets_sql_values.append(column[0])
                    property_id = check_serial_number(conn, table_list[0], properties_sql_insert, properties_sql_values)
                    check_asset_id(conn, table_list[1], asset_sql_insert, assets_sql_values, property_id)
                    # break

if __name__ == '__main__':
    main()