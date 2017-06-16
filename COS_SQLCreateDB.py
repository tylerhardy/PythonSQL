#! Python3
import sqlite3

def CreateDB(db_file):
    """Build the inventory database"""
    # Table Variables
    table_hardware = 'pc_hardware'
    table_properties = 'pc_properties'

    # pc_hardware column variable names
    pc_id = 'id'

    # pc_properties column Variable names
    properties_id = 'id'

    # column data type for hardware_inv table
    field_type_int = 'INTEGER'

    # Connecting to the database file
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Creating a new SQLite tables
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_hardware, nf=pc_id, ft=field_type_int))
    c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_properties, nf=properties_id, ft=field_type_int))

    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()

def UpdateTable(db_file):
    """Update the inventory database"""
    table_hardware = 'pc_hardware'
    table_properties = 'pc_properties'

    # pc_hardware columns
    asset_tag = 'asset_tag'
    name = 'name'
    owner = 'owner'
    curator = 'curator'
    location = 'location'
    department = 'department'
    organization_code = 'organization_code'
    make = 'make'
    model = 'model'
    pc_type = 'type'
    serial_number = 'serial_number'
    mac_wird = 'mac_wired'
    mac_wireless = 'mac_wireless'
    os = 'os'
    processor = 'processor'
    harddrvie = 'harddrvie'
    ram = 'ram'
    video_card = 'video_card'
    vendor = 'vendor'
    vendor_serial_number = 'vendor_serial_number'
    po = 'po'
    funded = 'funded'
    purchase_date = 'purchase_date'
    cost = 'cost'

    # column data type for hardware_inv table
    field_type_int = 'INTEGER'
    field_type_var = 'VARCHAR'
    field_type_date = 'DATE'
    field_type_text = 'TEXT'

    # pc_properties column Variable names
    pc_lifecycle = 'pc_lifecycle'
    property_control = 'proptery_control'
    active_directory = 'active_directory'
    sccm = 'sccm'
    jamf = 'jamf'

    # Connecting to the database file
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # A) Adding a new column without a row value
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=asset_tag, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=name, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=owner, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=curator, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=location, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=department, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=organization_code, ct=field_type_int))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=make, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=model, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=pc_type, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=serial_number, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=mac_wird, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=mac_wireless, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=os, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=processor, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=harddrvie, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=ram, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=video_card, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=vendor, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=vendor_serial_number, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=po, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=funded, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=vendor, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_hardware, cn=vendor, ct=field_type_var))

    # B) Adding a new column with a default row value
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_properties, cn=pc_lifecycle, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_properties, cn=property_control, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_properties, cn=active_directory, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_properties, cn=sccm, ct=field_type_var))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=table_properties, cn=jamf, ct=field_type_var))

    # Committing changes and closing the connection to the database file
    conn.commit()
    conn.close()

sqlite_file = 'cos_inventory_db.sqlite'

CreateDB(sqlite_file)
