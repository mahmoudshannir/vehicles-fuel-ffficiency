import sqlite3
conn = sqlite3.connect('VehiclesFuelEfficiency.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE tblUser (
        User_ID INTEGER PRIMARY KEY,
        First_Name TEXT NOT NULL,
        Last_Name TEXT NOT NULL,
        Username TEXT UNIQUE NOT NULL,
        Email TEXT NOT NULL,
        Phone_Number INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
''')
conn.commit()

c.execute('''
    CREATE TABLE tblCredential (
        User_ID INTEGER PRIMARY KEY,
        Username TEXT UNIQUE NOT NULL,
        Password TEXT NOT NULL,
        Datetime_Last_Login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(Username) REFERENCES tblUser(Username)
    );
''')
conn.commit()

#tbl_vehicle_category
c.execute('''
    CREATE TABLE tbl_vehicle_category (
        Category_ID INTEGER PRIMARY KEY,
        Category TEXT NOT NULL
    );
''')
conn.commit()

#tbl_vehicle_drivetrain
c.execute('''
    CREATE TABLE tbl_vehicle_drivetrain (
        Drivetrain_ID INTEGER PRIMARY KEY,
        Drivetrain TEXT NOT NULL
    );
''')
conn.commit()

#tbl_vehicle_engine_cylinder
c.execute('''
    CREATE TABLE tbl_vehicle_engine_cylinder (
        Engine_Cylinder_ID INTEGER PRIMARY KEY,
        Engine_Cylinder TEXT NOT NULL
    );
''')
conn.commit()

#tbl_vehicle_engine_size
c.execute('''
    CREATE TABLE tbl_vehicle_engine_size (
        Engine_Size_ID INTEGER PRIMARY KEY,
        Engine_Size TEXT NOT NULL
    );
''')
conn.commit()

#tbl_vehicle_engine_type
c.execute('''
    CREATE TABLE tbl_vehicle_engine_type (
        Engine_Type_ID INTEGER PRIMARY KEY,
        Engine_Type TEXT NOT NULL
    );
''')
conn.commit()

#tbl_vehicle_fuel
c.execute('''
    CREATE TABLE tbl_vehicle_fuel (
        Fuel_ID INTEGER PRIMARY KEY,
        Fuel TEXT NOT NULL
    );
''')
conn.commit()

#tbl_vehicle_manufacturer
c.execute('''
    CREATE TABLE tbl_vehicle_manufacturer (
        Manufacturer_ID INTEGER PRIMARY KEY,
        Manufacturer TEXT NOT NULL
    );
''')
conn.commit()

#tbl_vehicle_model
c.execute('''
    CREATE TABLE tbl_vehicle_model (
        Model_ID INTEGER PRIMARY KEY,
        Model TEXT NOT NULL
    );
''')
conn.commit()

#tbl_vehicle_transmission
c.execute('''
    CREATE TABLE tbl_vehicle_transmission (
        Transmission_Type_ID INTEGER PRIMARY KEY,
        Transmission_Type TEXT NOT NULL
    );
''')
conn.commit()

#tbl_vehicle_fuel_efficiency
c.execute('''
    CREATE TABLE tbl_vehicle_fuel_efficiency (
        ID INTEGER PRIMARY KEY,
        Category_ID INTEGER NOT NULL,
        Model_ID INTEGER NOT NULL,
        Model_Year INTEGER NOT NULL,
        Manufacturer_ID INTEGER NOT NULL,
        Fuel_ID TEXT INTEGER NULL,
        Drivetrain_ID INTEGER NOT NULL,
        Transmission_Type_ID INTEGER NOT NULL,
        Engine_Type_ID INTEGER NOT NULL,
        Engine_Size_ID INTEGER NOT NULL,
        Engine_Cylinder_ID INTEGER NOT NULL,
        Conventional_Fuel_Economy_City TEXT NOT NULL,
        Conventional_Fuel_Economy_Highway TEXT NOT NULL,
        Conventional_Fuel_Economy_Combined TEXT NOT NULL,
        FOREIGN KEY(Category_ID) REFERENCES tbl_vehicle_category(Category_ID),
        FOREIGN KEY(Model_ID) REFERENCES tbl_vehicle_model(Model_ID),
        FOREIGN KEY(Manufacturer_ID) REFERENCES tbl_vehicle_manufacturer(Manufacturer_ID),
        FOREIGN KEY(Fuel_ID) REFERENCES tbl_vehicle_fuel(Fuel_ID),
        FOREIGN KEY(Drivetrain_ID) REFERENCES tbl_vehicle_drivetrain(Drivetrain_ID),
        FOREIGN KEY(Transmission_Type_ID) REFERENCES tbl_vehicle_transmission(Transmission_Type_ID),
        FOREIGN KEY(Engine_Type_ID) REFERENCES tbl_vehicle_engine_type(Engine_Type_ID),
        FOREIGN KEY(Engine_Size_ID) REFERENCES tbl_vehicle_engine_size(Engine_Size_ID),
        FOREIGN KEY(Engine_Cylinder_ID) REFERENCES tbl_vehicle_engine_cylinder(Engine_Cylinder_ID)
    );
''')
conn.commit()

conn.close()
