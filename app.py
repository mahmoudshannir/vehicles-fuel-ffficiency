from flask import Flask,render_template,request,redirect, url_for,flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route("/")
def homepage():
    return render_template("Login.html")

@app.route('/FuelCostCalculator', methods=['GET', 'POST'])
def FuelCostCalculator():
    if request.method == 'POST':
        return render_template('FuelCostCalculator.html')

@app.route("/",methods = ['GET','POST'])
def login():
    username=request.form['Username']
    password=request.form['Password']

    errors =[]

    if not username:
        errors.append('Please enter your Username')
        
    if not password:
        errors.append('Please enter your Password')

    if errors:
        return render_template('login.html', errors=errors)
    
    else:

        # connect to the database
        conn = sqlite3.connect('VehiclesFuelEfficiency.db')
        cursor = conn.cursor()
        query1 = "SELECT Username,Password FROM tblCredential WHERE Username = '{un}' AND Password='{pw}'".format(un=username,pw=password)
        
        rows = cursor.execute(query1)
        rows = rows.fetchall()
        success_msg = []
        
        if len(rows) ==1:
            # connect to the database
            conn = sqlite3.connect('VehiclesFuelEfficiency.db')
            cursor = conn.cursor()

            # get all items from the database
            cursor.execute("""select ID,
            Category,
            Drivetrain,
            Model_Year,
            Engine_Cylinder,
            Engine_Size,
            Engine_Type,
            Fuel,
            Manufacturer,
            Model,
            Transmission_Type,
            Conventional_Fuel_Economy_City,
            Conventional_Fuel_Economy_Highway,
            Conventional_Fuel_Economy_Combined
            from vw_get_vehicles_data;
            """) 

            items = cursor.fetchall()

            success_msg.append('Login Successful')
            # render the index template with the items data
            if username =='Admin':
                return render_template('VehiclesFuelEfficiency.html', items=items,success_msg=success_msg)
            else:
              return render_template('VehiclesFuelEfficiencyView.html', items=items,success_msg=success_msg)  
        else:
            errors.append('Please Enter a Valid Username and Password')
            return render_template('login.html', errors=errors)

@app.route("/VehiclesFuelEfficiency")
def VehiclesFuelEfficiency():
    # connect to the database
    conn = sqlite3.connect('VehiclesFuelEfficiency.db')
    cursor = conn.cursor()

    # get all items from the database
               # get all items from the database
    cursor.execute("""select ID,
            Category,
            Drivetrain,
            Model_Year,
            Engine_Cylinder,
            Engine_Size,
            Engine_Type,
            Fuel,
            Manufacturer,
            Model,
            Transmission_Type,
            Conventional_Fuel_Economy_City,
            Conventional_Fuel_Economy_Highway,
            Conventional_Fuel_Economy_Combined
            from vw_get_vehicles_data;
            """) 
    items = cursor.fetchall()

    # render the index template with the items data
    return render_template('VehiclesFuelEfficiency.html', items=items)


@app.route('/register',methods = ["GET","POST"])
def register():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        phonenumber = request.form['phonenumber']
        password=request.form['password']
        confirm_password = request.form['confirm_password']

        # connect to the database
        conn = sqlite3.connect('VehiclesFuelEfficiency.db')
        cursor = conn.cursor()

        errors =[]
                
        # validate the form data
        if not username or not password or not confirm_password or not email:
            errors.append('All fields are required')

        if password != confirm_password:
            errors.append('Passwords do not match')
        
        # check if the username or email is already registered
        query = "SELECT * FROM tblUser WHERE username = ? OR email = ?"
        cursor.execute(query, (username, email))
        if cursor.fetchone():
            errors.append('Username or email already registered')
        
        if errors:
            return render_template('Register.html', errors=errors)
        
        else:
            # insert the user data into the database
            cursor.execute("INSERT INTO tblUser (First_Name ,Last_Name,Username,Email,Phone_Number) VALUES(?,?,?,?,?)",(firstname , lastname ,username, email,phonenumber))
            conn.commit()

            cursor.execute("INSERT INTO tblCredential (Username,Password) VALUES(?,?)",(username,password))
            conn.commit()
            success_r = []
            # return "Registration successful"
            return redirect(url_for('login'))
            success_r.append('Account Registered Successfully. Please login')
    return render_template("Register.html")
    
@app.route('/edit_item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    # connect to the database
    conn = sqlite3.connect('VehiclesFuelEfficiency.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        # update the item in the database
        category = request.form['category']
        drivetrain = request.form['drivetrain']
        year = request.form['year']
        cylinder = request.form['cylinder']
        size = request.form['size']
        type = request.form['type']
        fuel = request.form['fuel']
        manufacturer = request.form['manufacturer']
        model = request.form['model']
        transmission = request.form['transmission']
        city = request.form['city']
        highway = request.form['highway']
        combined = request.form['combined']

        # validate the form data
        
        errors =[]

        if not category or not drivetrain or not  year or not cylinder or not  size or not  type or not  fuel or not  manufacturer or not  model or not  transmission or not  city or not  highway or not  combined:
            errors.append('All fields are required')
        if errors:
            return render_template('Edit.html', errors=errors)
        else:

            cursor.execute("select Category_ID from tbl_vehicle_category where Category=?", (category,))
            category = cursor.fetchone()

            cursor.execute("select Drivetrain_ID  from tbl_vehicle_drivetrain  where Drivetrain=?", (drivetrain,))
            drivetrain = cursor.fetchone()
                
            cursor.execute("select Engine_Cylinder_ID from tbl_vehicle_engine_cylinder  where Engine_Cylinder=?", (cylinder,))
            cylinder = cursor.fetchone()

            cursor.execute("select Engine_Type_ID   from tbl_vehicle_engine_type   where Engine_Type =?", (type ,))
            type = cursor.fetchone()

            cursor.execute("select Fuel_ID   from tbl_vehicle_fuel   where Fuel =?", (fuel ,))
            fuel = cursor.fetchone()

            cursor.execute("select Transmission_Type_ID   from tbl_vehicle_transmission   where Transmission_Type =?", (transmission ,))
            transmission = cursor.fetchone()

            category = category[0]
            drivetrain = drivetrain[0]
            cylinder = cylinder[0]
            type = type[0]
            fuel = fuel[0]
            transmission = transmission[0]

            cursor.execute("UPDATE tbl_vehicle_fuel_efficiency SET Category_ID=?,Model_ID=?,Model_Year=?,Manufacturer_ID=?,Fuel_ID=?,Drivetrain_ID=?,Transmission_Type_ID=?,Engine_Type_ID=?,Engine_Size_ID=?,Engine_Cylinder_ID=?,Conventional_Fuel_Economy_City=?,Conventional_Fuel_Economy_Highway=?,Conventional_Fuel_Economy_Combined=? WHERE id=?",(category,drivetrain, year,cylinder, size, type, fuel, manufacturer, model, transmission, city, highway, combined, item_id))
            conn.commit()

        # redirect back to the index page
            return redirect(url_for('VehiclesFuelEfficiency'))
    else:
        # get the item from the database
        cursor.execute('SELECT * FROM tbl_vehicle_fuel_efficiency WHERE id=?', (item_id,))
        item = cursor.fetchone()

        # render the edit template with the item data
        return render_template('edit.html', item=item)

@app.route('/delete_item/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    # connect to the database
    conn = sqlite3.connect('VehiclesFuelEfficiency.db')
    cursor = conn.cursor()

    # delete the item from the database
    cursor.execute('DELETE FROM tbl_vehicle_fuel_efficiency WHERE id=?', (item_id,))
    conn.commit()

    # redirect back to the index page
    return redirect(url_for('VehiclesFuelEfficiency'))

@app.route('/add_item',methods = ["GET","POST"])# methods=['POST'])
def add_item():
    if request.method == "POST":
        category = request.form['category']
        drivetrain = request.form['drivetrain']
        year = request.form['year']
        cylinder = request.form['cylinder']
        size = request.form['size']
        type = request.form['type']
        fuel = request.form['fuel']
        manufacturer = request.form['manufacturer']
        model = request.form['model']
        transmission = request.form['transmission']
        city = request.form['city']
        highway = request.form['highway']
        combined = request.form['combined']

        # validate the form data
        
        errors =[]

        if not category or not drivetrain or not  year or not cylinder or not  size or not  type or not  fuel or not  manufacturer or not  model or not  transmission or not  city or not  highway or not  combined:
            errors.append('All fields are required')
        if errors:
            return render_template('Add_Item.html', errors=errors)
        
        else:

            # connect to the database
            conn = sqlite3.connect('VehiclesFuelEfficiency.db')
            cursor = conn.cursor()


            cursor.execute("select Category_ID from tbl_vehicle_category where Category=?", (category,))
            category = cursor.fetchone()

            cursor.execute("select Drivetrain_ID  from tbl_vehicle_drivetrain  where Drivetrain=?", (drivetrain,))
            drivetrain = cursor.fetchone()
                
            cursor.execute("select Engine_Cylinder_ID from tbl_vehicle_engine_cylinder  where Engine_Cylinder=?", (cylinder,))
            cylinder = cursor.fetchone()

            cursor.execute("select Engine_Type_ID   from tbl_vehicle_engine_type   where Engine_Type =?", (type ,))
            type = cursor.fetchone()

            cursor.execute("select Fuel_ID   from tbl_vehicle_fuel   where Fuel =?", (fuel ,))
            fuel = cursor.fetchone()

            cursor.execute("select Transmission_Type_ID   from tbl_vehicle_transmission   where Transmission_Type =?", (transmission ,))
            transmission = cursor.fetchone()

            category = category[0]
            drivetrain = drivetrain[0]
            cylinder = cylinder[0]
            type = type[0]
            fuel = fuel[0]
            transmission = transmission[0]

            cursor.execute("INSERT INTO tbl_vehicle_fuel_efficiency (Category_ID,Model_ID,Model_Year,Manufacturer_ID,Fuel_ID,Drivetrain_ID,Transmission_Type_ID,Engine_Type_ID,Engine_Size_ID,Engine_Cylinder_ID,Conventional_Fuel_Economy_City,Conventional_Fuel_Economy_Highway,Conventional_Fuel_Economy_Combined) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(category,drivetrain, year,cylinder, size, type, fuel, manufacturer, model, transmission, city, highway, combined))
            conn.commit()

            return redirect(url_for('VehiclesFuelEfficiency'))
    return render_template("Add_Item.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run()