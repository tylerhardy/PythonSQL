import os, csv, datetime
import sqlite3
from sqlite3 import Error

"""
1. Grab headers
2. Map headers to db columns
3. Check if key column has value
    if value - new dict > add key (asset_tag) value (WS0002131) to 

    else pass
"""
TABLE_PROPERTIES = 'properties'
TABLE_ASSETS = 'assets'

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

def create_properties(conn, values):
 
    query_value = ''' INSERT INTO properties(type,mac_wired,mac_wireless,serial_number) VALUES(?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(query_value, values)
    return cur.lastrowid

def main():
    database = "cos_inventory.db"

    conn = create_connection(database)
    with conn:
        """ Next revision, change table then prop in dict"""
        excel_dict = {
            'D_TYPE' : [TABLE_PROPERTIES, 'type'],
            'D_MAC_WIRED' : [TABLE_PROPERTIES, 'mac_wired'],
            'D_MAC_WIRELESS' : [TABLE_PROPERTIES, 'mac_wireless'],
            'D_SERIAL_NUM' : [TABLE_PROPERTIES, 'serial_number'],
            'D_CODE' : [TABLE_ASSETS, 'asset_tag'],
            'D_AMT'	: [TABLE_ASSETS, 'cost'],
            'D_ACQD_DATE' : [TABLE_ASSETS, 'purchase_date'],
            'D_PO' : [TABLE_ASSETS, 'po'],
            'D_ORGN_CODE' : [TABLE_ASSETS, 'organization_code'],
            'T_ORGN_CODE_DESC' : [TABLE_ASSETS, 'department'],
            'D_LOCN_CODE_RESP' : [TABLE_ASSETS, 'location'],
            'D_DESC' : [TABLE_ASSETS, 'description'],
            'D_DEVICE_OWNER' : [TABLE_ASSETS, 'owner']
        }
        """Searches fo CSV files and create a list with its contents"""
        for csvFilename in os.listdir('.'):
            if not csvFilename.endswith('.csv'):
                continue
            with open(csvFilename,'r') as csvFileObj:
                _EXCEL_FILE_OBJECT = csv.reader(csvFileObj)

                EXCEL_TOP_ROW = next(_EXCEL_FILE_OBJECT)
                PROPERTIES_LIST = []

                for data_row in _EXCEL_FILE_OBJECT:
                    SQL_DICT = {TABLE_PROPERTIES:[], TABLE_ASSETS:[]}
                    for index, item in enumerate(data_row):
                        SQL_IDENTIFIER = excel_dict.get(EXCEL_TOP_ROW[index])
                        if SQL_IDENTIFIER is not None:
                            if str(item).lower().strip() is not "":
                                if SQL_IDENTIFIER[0] == TABLE_ASSETS:
                                    SQL_DICT[TABLE_ASSETS].append([item, SQL_IDENTIFIER[1]])
                                elif SQL_IDENTIFIER[0] == TABLE_PROPERTIES:
                                    SQL_DICT[TABLE_PROPERTIES].append([item, SQL_IDENTIFIER[1]])
                    _ASSET_TAG_ID = ""
                    sql_insert = []
                    sql_values = []
                    property_id = -1
                    for table, columns in SQL_DICT.items():
                        for column in columns:
                            sql_insert.append(column[1])
                            sql_values.append(column[0])
                        if table == TABLE_PROPERTIES:
                            property_id = check_serial_number(conn, table, sql_insert, sql_values)
                            print(sql_insert)
                            print(sql_values)
                        elif table == TABLE_ASSETS:
                            check_asset_id(conn, table, sql_insert, sql_values, property_id)
                            property_id = -1
                            print(sql_insert)
                            print(sql_values)
                        print('\n')
                    break

def check_serial_number(conn, table, insert, values):
    asset_index = (insert.index('serial_number'))
    asset_value = values[asset_index]
    query = "SELECT id, serial_number FROM properties WHERE serial_number='{0}';".format(asset_value)
    cur = conn.cursor()
    cur.execute(query)
    serial_row = cur.fetchone()
    if serial_row is None:
        print('Execute insert query')
        return _get_or_insert(conn, table, insert, values, -1)
    else:
        print('Already exists')
        return serial_row[0]

def check_asset_id(conn, table, insert, values, id):
    asset_index = (insert.index('asset_tag'))
    asset_value = values[asset_index]
    query = "SELECT id, asset_tag FROM assets WHERE asset_tag='{0}';".format(asset_value)
    cur = conn.cursor()
    cur.execute(query)
    serial_row = cur.fetchone()
    if serial_row is None:
        print('Execute insert query')
        return _get_or_insert(conn, table, insert, values, id)
    else:
        print('Already exists')
        return serial_row[0]

def _get_or_insert(conn, table, insert, values, id):
    # get_query = 'SELECT {0} FROM {1}'.format()
    insert_object_id = ""
    insert = ', '.join(insert)
    values = "'" + "','".join(values) + "'"
    query_string = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(table,insert,values)
    # print(query_string)
    # cur = conn.cursor()
    # cur.execute(query_string)
    # return cur.lastrowid
    

if __name__ == '__main__':
    main()