import csv
import sqlite3

# Connect to the SQLite database and create a new table
conn = sqlite3.connect('VehiclesFuelEfficiency.db')
cursor = conn.cursor()

# tbl_vehicle_category
with open('DataTables/tbl_vehicle_category.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_category")
conn.commit()
cursor.executemany("INSERT INTO tbl_vehicle_category (Category_ID,Category) VALUES(?,?)",data)
conn.commit()

# tbl_vehicle_drivetrain 
with open('DataTables/tbl_vehicle_drivetrain.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_drivetrain")
conn.commit()
cursor.executemany("INSERT INTO tbl_vehicle_drivetrain  (Drivetrain_ID,Drivetrain) VALUES(?,?)",data)
conn.commit()

# tbl_vehicle_engine_cylinder
with open('DataTables/tbl_vehicle_engine_cylinder.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_engine_cylinder")
conn.commit()
cursor.executemany("INSERT INTO tbl_vehicle_engine_cylinder (Engine_Cylinder_ID,Engine_Cylinder) VALUES(?,?)",data)
conn.commit()

# tbl_vehicle_engine_size
with open('DataTables/tbl_vehicle_engine_size.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_engine_size")
conn.commit()
cursor.executemany("INSERT INTO tbl_vehicle_engine_size (Engine_Size_ID,Engine_Size) VALUES(?,?)",data)
conn.commit()

# tbl_vehicle_engine_type
with open('DataTables/tbl_vehicle_engine_type.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_engine_type")
conn.commit()
cursor.executemany("INSERT INTO tbl_vehicle_engine_type (Engine_Type_ID,Engine_Type) VALUES(?,?)",data)
conn.commit()

# tbl_vehicle_fuel 
with open('DataTables/tbl_vehicle_fuel.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_fuel")
conn.commit()
cursor.executemany("INSERT INTO tbl_vehicle_fuel (Fuel_ID,Fuel) VALUES(?,?)",data)
conn.commit()

# tbl_vehicle_manufacturer 
with open('DataTables/tbl_vehicle_manufacturer.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_manufacturer")
conn.commit()
cursor.executemany("INSERT INTO tbl_vehicle_manufacturer (Manufacturer_ID,Manufacturer) VALUES(?,?)",data)
conn.commit()

# tbl_vehicle_model
with open('DataTables/tbl_vehicle_model.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_model")
conn.commit()
cursor.executemany("INSERT INTO tbl_vehicle_model (Model_ID,Model) VALUES(?,?)",data)
conn.commit()

# tbl_vehicle_transmission
with open('DataTables/tbl_vehicle_transmission.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_transmission")
conn.commit()
cursor.executemany("INSERT INTO tbl_vehicle_transmission (Transmission_Type_ID,Transmission_Type) VALUES(?,?)",data)
conn.commit()

# Open the CSV file and read its contents
with open('DataTables/tbl_vehicle_fuel_efficiency.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    data = [tuple(row) for row in reader]

cursor.execute("Delete from tbl_vehicle_fuel_efficiency")
conn.commit()
cursor.executemany("""INSERT INTO tbl_vehicle_fuel_efficiency 
                        (ID,
                        Category_ID,
                        Model_ID,
                        Model_Year,
                        Manufacturer_ID,
                        Fuel_ID,
                        Drivetrain_ID,
                        Transmission_Type_ID,
                        Engine_Type_ID,
                        Engine_Size_ID,
                        Engine_Cylinder_ID,
                        Conventional_Fuel_Economy_City,
                        Conventional_Fuel_Economy_Highway,
                        Conventional_Fuel_Economy_Combined 
                        ) 
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",data)
conn.commit()

#Close Connection
conn.close()
