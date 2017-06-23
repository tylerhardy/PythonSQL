#!/usr/bin/python

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

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "C:\\Users\\tylerhardy\\Developer\\PythonSql\\cos_inventory.db"

    sql_create_hardware_table = """ CREATE TABLE IF NOT EXISTS hardware (
                                    id integer PRIMARY KEY,
                                    make text,
                                    model text,
                                    type text,
                                    serial_number text,
                                    mac_wired text,
                                    mac_wireless text,
                                    processor text,
                                    harddrvie text,
                                    ram text,
                                    video_card text,
                                    notes text,
                                    added_date text,
                                    modified_date text
                                ); """

    sql_create_assets_table = """ CREATE TABLE IF NOT EXISTS assets (
                                    id integer PRIMARY KEY,
                                    hardware_id integer NOT NULL,
                                    asset_tag text NOT NULL,
                                    owner text,
                                    curator text,
                                    location text,
                                    department text,
                                    organization_code integer,
                                    vendor text,
                                    vendor_serial_number text,
                                    po text,
                                    funded text,
                                    purchase_date text,
                                    cost real,
                                    notes text,
                                    added_date text,
                                    modified_date text,
                                    FOREIGN KEY (hardware_id) REFERENCES hardware (id)
                                ); """

    sql_create_software_table = """ CREATE TABLE IF NOT EXISTS software (
                                    id integer PRIMARY KEY,
                                    asset_id integer NOT NULL,
                                    computer_name text,
                                    os text,
                                    pc_lifecycle text,
                                    pc_lifecycle_update text,
                                    proptery_control text,
                                    proptery_control_update text,
                                    active_directory_ou text,
                                    sccm_db text,
                                    jamf_db text,
                                    scep text,
                                    identity_finder text,
                                    sc_ss text,
                                    notes text,
                                    added_date text,
                                    modified_date text,
                                    FOREIGN KEY (asset_id) REFERENCES assets (id)
                                ); """

    # Create a database connection
    conn = create_connection(database)
    if conn is not None:
        # Create assets table
        create_table(conn, sql_create_assets_table)
        # Create hardware table
        create_table(conn, sql_create_hardware_table)
        # Create software table
        create_table(conn, sql_create_software_table)
    else:
        print("Error! Cannot create the database connection.")

    # create a database connection
    conn = create_connection(database)

    # Create a database connection
    conn = create_connection(database)
    if conn is not None:
        # Create assets table
        create_table(conn, sql_create_assets_table)
        # Create hardware table
        create_table(conn, sql_create_hardware_table)
        # Create software table
        create_table(conn, sql_create_software_table)
    else:
        print("Error! Cannot create the database connection.")

    conn.close()

if __name__ == '__main__':
    main()