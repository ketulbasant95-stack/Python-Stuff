import mysql.connector as sqlcon
from prettytable import PrettyTable as pt
import os

#definition of connection and cursor objects
mycon = sqlcon.connect(host = "localhost", user = "root", passwd = "1234", database = "science")
sqlcur = mycon.cursor()

#one-time run of table creation code
#sqlcur.execute("create table manufacturers(Manufacturer_ID char(3) primary key, Manufacturer_Name varchar(12) not null, Country varchar(15));")
#sqlcur.execute("create table cars(Car_ID char(3) primary key, Manufacturer_ID char(3), Model varchar(15) not null, Year char(4), Engine_Displacement float, Engine_Layout char(3), Brake_Horsepower float, Torque float, Transmission char(2), Fuel_Type char(1), Drivetrain char(3), Price int, Availability char(1));")
#sqlcur.execute("create table sales(Sale_ID char(4) primary key, Car_ID char(3), Customer_ID char(4), Sales_Date date, Price int, Payment_Status char(1));")
#sqlcur.execute("create table customers(Customer_ID char(4) primary key, Cust_Name varchar(15) not null, Phone_No int, Email varchar(50));")

#Add functions: adds values to defined tables
def addToManufacturers():
    while True:
        manID = input("Enter manufacturer ID: ")
        mName = input("Enter manufacturer name: ")
        country = input("Enter country of origin: ")

        sqlcur.execute("insert into manufacturers values(%s,%s,%s)", (manID, mName, country))
        mycon.commit()
        
        if input("Continue? (Y/N): ") not in "Yy":
            break
        
def addToCars():
    carID = input("Enter car ID: ")
    mID = input("Enter manufacturer ID: ")
    model = input("Enter model: ")
    year = input("Enter year of make: ")
    cc = float(input("Enter engine displacement: "))
    engConfig = input("Enter engine layout: ")
    bhp = float(input("Enter brake horsepower: "))
    nm = float(input("Enter torque: "))
    gears = input("Enter transmission data: ")
    ftype = input("Enter fuel type (P/D/C/E): ")
    dTrain = input("Enter drivetrain configuration (FWD/RWD/4WD/AWD): ")
    price = int(input("Enter base price: "))
    status = input("In stock? (Y/N): ")

    sqlcur.execute("insert into cars values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (carID, mID, model, year, cc, engConfig, bhp, nm, gears, ftype, dTrain, price, status))
    mycon.commit()
    
def addToCust():
    while True:
        custID = input("Enter customer ID: ")
        custName = input("Enter customer name: ")
        phno = input("Enter phone number: ")
        mail = input("Enter e-mail address: ")

        sqlcur.execute("insert into customers values(%s,%s,%s,%s)", (custID, custName, phno, mail))

        if input("Continue? (Y/N): ") not in "Yy":
            break
        mycon.commit()
        
def addToSales():
    salesID = input("Enter sales ID: ")
    carID = input("Enter car ID: ")
    custID = input("Enter customer ID: ")
    sDate = input("Enter sales date (YYYY/MM/DD): ")
    price = int(input("Enter total amount: "))
    status = input("Payment completed? (Y/N): ")

    sqlcur.execute("insert into sales values(%s,%s,%s,%s,%s,%s)", (salesID, carID, custID, sDate, price, status))
    mycon.commit()
    
#Modify functions: modifies selected attribute
def modifyManufacturers():
    manID = input("Enter manufacturer ID whose data is to be modified: ")
    print("Select attribute to modify...\n" \
    "1. Manufacturer\n" \
    "2. Country")

    att = {1: "Manufacturers",
           2: "Country"}
    while True:
        ch = int(input("Enter your choice: "))
        if ch in att:
            col = att[ch]
            newVal = input(f"Enter new value for {col}: ")        

            sqlcur.execute(f"update manufacturers set {col} = {newVal} where manufacturerID = {manID}")
        else:
            print("Invalid choice, try again...")

        if input("Continue? (Y/N): ") not in "Yy":
            break

def modifyCars():
    carID = input("Enter car ID whose data is to be modified: ")
    print("Select attribute to modify...\n" \
    "1. Manufacturer ID\n" \
    "2. Model" \
    "3. Year\n" \
    "4. Engine Displacement\n" \
    "5. Engine layout\n" \
    "6. Horsepower\n" \
    "7. Torque\n" \
    "8. Transmission\n" \
    "9. Fuel type\n" \
    "10. Drivetrain\n" \
    "11. Base price\n" \
    "12. Availability")

    att = {
    1: ("Manufacturer_ID", "Enter new manufacturer ID: ", str),
    2: ("Model", "Enter new model: ", str),
    3: ("Year", "Enter new year: ", str),
    4: ("Engine_Displacement", "Enter new engine displacement: ", float),
    5: ("Engine_Layout", "Enter new engine layout: ", str),
    6: ("Brake_Horsepower", "Enter new horsepower: ", float),
    7: ("Torque", "Enter new torque: ", float),
    8: ("Transmission", "Enter new transmission: ", str),
    9: ("Fuel_Type", "Enter new fuel type: ", str),
    10: ("Drivetrain", "Enter new drivetrain: ", str),
    11: ("Price", "Enter new base price: ", int),
    12: ("Availability", "Available? (Y/N): ", str)}

    while True:
        ch = int(input("Enter your choice: "))
        if ch in att:
            col, text, dType = att[ch]
            newVal = dType(input(text))

            sqlcur.execute(f"update cars set {col} = {newVal} where car_ID = {carID}")
        else:
            print("Invalid choice, try again...")

        if input("Continue? (Y/N): ") not in "Yy":
            break


def modifyCust():
    custID = input("Enter customer ID whose attributes have to be modified: ")
    print("Select attribute to modify...\n" \
    "1. Customer name\n" \
    "2. Phone number\n" \
    "3. E-mail address")

    att = {1: ("Cust_name", "Enter new customer name: ", str),
           2: ("Phone_no", "Enter new phone number: ", str),
           3: ("Email", "Enter new e-mail address: ", str)}

    while True:
        ch = int(input("Enter your choice: "))
        if ch in att:
            col, text, dtype = att[ch]
            newVal = dtype(input(text))

            sqlcur.execute("update customers set email = %s where customer_ID = %s;", (newVal, custID))
            mycon.commit()
        else:
            print("Invalid choice, try again...")
        if input("Continue? (Y/N): ") not in "Yy":
            break

def modifySales():
    salesID = input("Enter sales ID whose attributes have to be modified: ")

    print("Select attribute to modify...\n" \
    "1. Car ID\n" \
    "2. Customer ID\n" \
    "3. Sales Date\n" \
    "4. Price\n" \
    "5. Payment completed?")

    att = {1: ("Car_ID", "Enter new car ID: ", str),
           2: ("Cust_ID", "Enter new customer ID: ", str),
           3: ("Sales_date", "Enter new sales date (YYYY-MM-DD): ", str),
           4: ("Price", "Enter new base price: ", int),
           5: ("Payment_status", "Payment completed? (Y/N): ", str)}
    while True:
        ch = int(input("Enter your choice: "))
        if ch in att:
            col, text, dtype = att[ch]
            newVal = dtype(input(text))

            sqlcur.execute(f"update sales set {col} = {newVal} where sales_ID = {salesID}")
        else:
            print("Invalid choice, try again...")
        if input("Continue? (Y/N): ") not in "Yy":
            break

#Search function: searches and displays entire table
def search():
    print("Select table...\n"\
          "1. Manufacturers\n"\
          "2. Cars\n"\
          "3. Customers\n"\
          "4. Sales")
    ch0 = input("Enter your choice: ")
    if ch0=="1":
        sqlcur.execute("select * from Manufacturers;")
        rec = sqlcur.fetchall()
        t = pt(["Manufacturer ID", "Manufacturer Name", "Country"])
        t.align["Manufacturer Name"] = "l"
        t.align["Country"] = "l"
        for data in rec:
            t.add_row(list(data))
        print(t)
    elif ch0=="2":
        sqlcur.execute("select * from cars;")
        rec =  sqlcur.fetchall()

        t = pt(["Car ID", "Manufacturer ID", "Model", "Year", "Engine Displacement", "Engine Layout", "Horsepower", "Torque", "Transmission", "Fuel Type", "Drivetrain", "Price", "Availability"])
        for data in rec:
            t.add_row(list(data))
        print(t)
    elif ch0=="3":
        sqlcur.execute("select * from customers;")
        rec = sqlcur.fetchall()
        t = pt(["Customer ID", "Customer Name", "Phone Number", "Email"])
        for data in rec:
            t.add_row(list(data))
        print(t)
    elif ch0=="4":
        sqlcur.execute("select * from sales;")
        rec = sqlcur.fetchall()
        t = pt(["Sales ID", "Car ID", "Customer ID", "Sales Date", "Proce", "Payment Completed"])
        for data in rec:
            t.add_row(list(data))
        print(t)
    else:
        print("Invalid choice, try again.")

#Delete function: deletes records from table by searching by ID
def delete():
    print("Delete table...\n"\
          "1. Manufacturers\n"\
          "2. Cars\n"\
          "3. Customers\n"\
          "4. Sales")
    ch = input("Enter your choice: ")
    if ch=="1":
        id = input("Enter manufacturer ID to delete: ")
        sqlcur.execute(f"delete from manufacturers where manufacturer_ID = {id};")
    elif ch=="2":
        id = input("Enter car ID to delete: ")
        sqlcur.execute(f"delete from manufacturers where car_ID = {id};")
    elif ch=="3":
        id = input("Enter customer ID to delete: ")
        sqlcur.execute(f"delete from manufacturers where cust_ID = {id};")
    elif ch=="4":
        id = input("Enter sales ID to delete: ")
        sqlcur.execute(f"delete from manufacturers where sales_ID = {id};")
    else:
        print("Invaid choice, try again.")
