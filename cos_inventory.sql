CREATE DATABASE IF NOT EXISTS 'cos_inventory';
USE 'cos_inventory';

CREATE TABLE IF NOT EXISTS 'assets' (
    'id' int(10) unsigend NOT NULL,
    'asset_tag' varchar(50) DEFAULT NOT NULL,
    'name' varchar(50) DEFAULT NULL,
    'owner' varchar(50) DEFAULT NULL,
    'curator' varchar(50) DEFAULT NULL,
    'location' varchar(50) DEFAULT NULL,
    'department' varchar(50) DEFAULT NULL,
    'organization_code' int(50) DEFAULT NULL,
    'make' varchar(50) DEFAULT NULL,
    'model' varchar(50) DEFAULT NULL,
    'type' varchar(50) DEFAULT NULL,
    'serial_number' varchar(50) DEFAULT NULL,
    'mac_wired' varchar(50) DEFAULT NULL,
    'mac_wireless' varchar(50) DEFAULT NULL,
    'os' varchar(50) DEFAULT NULL,
    'processor' varchar(50) DEFAULT NULL,
    'harddrvie' varchar(50) DEFAULT NULL,
    'ram' varchar(50) DEFAULT NULL,
    'video_card' varchar(50) DEFAULT NULL,
    'vendor' varchar(50) DEFAULT NULL,
    'vendor_serial_number' varchar(50) DEFAULT NULL,
    'po' varchar(50) DEFAULT NULL,
    'funded' varchar(50) DEFAULT NULL,
    'purchase_date' date DEFAULT NULL,
    'cost' int(50) DEFAULT NULL,
    PRIMARY KEY ()

)

CREATE TABLE IF NOT EXISTS 'properties' (
    'pc_lifecycle'
    'proptery_control'
    'active_directory'
    'sccm'
    'jamf'
)