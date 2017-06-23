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
        excel_dict = {
            'D_TYPE' : ['type', 'properties'],
            'D_MAC_WIRED' : ['mac_wired', 'properties'],
            'D_MAC_WIRELESS' : ['mac_wireless', 'properties'],
            'D_SERIAL_NUM' : ['serial_number', 'properties'],
            'D_CODE' : ['asset_tag', 'assets'],
            'D_AMT'	: ['cost', 'assets'],
            'D_ACQD_DATE' : ['purchase_date', 'assets'],
            'D_PO' : ['po', 'assets'],
            'D_ORGN_CODE' : ['organization_code', 'assets'],
            'T_ORGN_CODE_DESC' : ['department', 'assets'],
            'D_LOCN_CODE_RESP' : ['location', 'assets'],
            'D_DESC' : ['description', 'assets'],
            'D_DEVICE_OWNER' : ['owner', 'assets']
        }
        """Searches fo CSV files and create a list with its contents"""
        for csvFilename in os.listdir('.'):
            if not csvFilename.endswith('.csv'):
                continue
            with open(csvFilename,'r') as csvFileObj:
                _EXCEL_FILE = csv.reader(csvFileObj)

                EXCEL_TOP_ROW = next(_EXCEL_FILE)
                PROPERTIES_LIST = []

                for data_row in _EXCEL_FILE:
                    SQL_DICT = {'properties':[], 'assets':[]}
                    for index, item in enumerate(data_row):
                        SQL_IDENTIFIER = excel_dict.get(EXCEL_TOP_ROW[index])
                        if SQL_IDENTIFIER is not None:
                            if str(item).lower().strip() is not "":
                                if SQL_IDENTIFIER[1] == 'assets':
                                    SQL_DICT['assets'].append([item, SQL_IDENTIFIER[0]])
                                elif SQL_IDENTIFIER[1] == 'properties':
                                    SQL_DICT['properties'].append([item, SQL_IDENTIFIER[0]])

                    # print(SQL_DICT)
                    sql_insert = ""
                    sql_values = ""
                    for table, column in SQL_DICT.items():
                        print(table)
                        for i in column:
                            sql_insert += i[1] + ', '
                            sql_values += i[0] + ', '
                        sql_insert = (sql_insert.strip()[:-1])
                        sql_values = (sql_values.strip()[:-1])
                        # print(sql_insert)
                        # print(sql_values)
                        create_property(table,sql_insert,sql_values)
                        sql_insert = ""
                        sql_values = ""
                        print('\n')
                    break

def create_property(table, insert, values):
    query_string = 'INSERT INTO {0} ({1}) VALUES ({2})'.format(table,insert,values)
    print(query_string)

if __name__ == '__main__':
    main()

    #         if row[type_id] == 'PC' or  row[type_id] == 'LT':
    #             var_list.append([row[asset_id]])
    #             dict_list[str(name_var)] = var_list
    # csvFileObj.close()