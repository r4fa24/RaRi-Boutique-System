# SECURITY NOTE: In a production environment, use environment variables 
# to store database credentials rather than hardcoding them.
import mysql.connector
from tabulate import tabulate
'''mydb=mysql.connector.connect(host="localhost",user='root',passwd='efia@123')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists RARIBOUTIQUE")
mycursor.execute("show databases")
for x in mycursor:
    print(x)'''


 
def createdtable():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='efia@123',database='RARIBOUTIQUE')
    mycursor=mydb.cursor()
    myrecords=mycursor.execute('Create table dress(Dcode char(5) primary key, Name varchar(30), Type varchar(20), Colour varchar(25),price int(5))')
    mycursor.execute('Desc dress')
    for x in mycursor:
        print(x)

def addrecord():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='efia@123',database='RARIBOUTIQUE')
    mycursor=mydb.cursor()
    n=int(input("Enter the number of records:"))
    try:
        for i in range(n):
            Dcode=input("Enter the dress code.")
            dname=input("Enter dress name: ")
            dtype=input("Enter the dress type: ")
            colour=input('Enter the colour: ')
            price=int(input("Enter price: "))
            q1="INSERT INTO DRESS VALUES ('{}','{}','{}','{}',{})".format(Dcode,dname,dtype,colour,price)
            mycursor.execute(q1)
            mydb.commit()
            print("*record added successfully*")
    except Exception as e:
        print("*record not added successfully*",e)
def fetchdatad():
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='efia@123',database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM DRESS")
        myrecords = mycursor.fetchall()
        headers = ["Dcode", "Name", "Type", "Colour", "Price"]
        table = tabulate(myrecords, headers, tablefmt="grid")
        print(table)
    except Exception as e:
        print("Unable to display\n", e)       
def editbydno():
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='efia@123',database='RARIBOUTIQUE')
        mycursor=mydb.cursor()
        reqdno=input("Enter the dress code: ")
        query="Select * from dress where Dcode='{}'".format(reqdno)
        mycursor.execute(query)
        results=mycursor.fetchall()
        headers = ["Dcode", "Name", "Type", "Colour", "Price"]
        table = tabulate(results, headers, tablefmt="grid")
        print(table)
        if mycursor.rowcount<=0:
            print('\## SORRY! NO MATCHING DETAILS AVAILABLE ##')
        else:
            ne=input("Enter new name to update (Enter old value if not to update) :")
            nt=input("Enter new type to update (Enter old value if not to update) :")
            nc=input("Enter new colour to update (Enter old value if not to update) :")
            pr=int(input("Enter new price to update (Enter old value if not to update) :"))
            query="update dress set name='{}',type='{}',colour='{}',price={} where Dcode='{}'".format(ne,nt,nc,pr,reqdno)
            mycursor.execute(query)
            mydb.commit()
            print("RECORD UPDATED ##")
    except Exception as e:
        print(e)        
def deletebydno():
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()

        reqdno = input("Enter the dress code to be deleted: ")
        query = "SELECT * FROM dress WHERE Dcode = '{}'".format(reqdno)
        mycursor.execute(query)
        results = mycursor.fetchall()

        if mycursor.rowcount <= 0:
            print('## SORRY! NO MATCHING DETAILS AVAILABLE ##')
        else:
            print('%7s' % 'Dcode', '%10s' % 'Name', '%7s' % 'Type', '%7s' % 'Colour', '%7s' % 'Price')
            for row in results:
                print('%7s' % row[0], '%10s' % row[1], '%7s' % row[2], '%7s' % row[3], '%7s' % row[4])
                print()

            ans = input("Do you want to delete? (y/n): ")
            if ans.lower() == 'y':
                delete_query = "DELETE FROM dress WHERE Dcode = '{}'".format(reqdno)
                mycursor.execute(delete_query)
                mydb.commit()
                print("Record Deleted")
            else:
                print("Not deleted")
    except Exception as e:
        print('SORRY NOT FOUND', e)
    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

            
def searchdbytype():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        reqrtype = input("Enter the type:")
        query = "SELECT * FROM dress WHERE Type='{}'".format(reqrtype)
        mycursor.execute(query)
        myrecords = mycursor.fetchall()
        headers = ["Dcode", "Name", "Type", "Colour", "Price"]
        table = tabulate(myrecords, headers, tablefmt="grid")
        print(table)
        '''if mycursor.rowcount <= 0:
            print("\n## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
            print('%10s' % 'Code', '%15s' % 'Name', '%10s' % 'Type', '%10s' % 'Colour', '%30s' % 'Price')
            for x in myrecords:
                print('%10s' % x[0], '%15s' % x[1], '%10s' % x[2], '%10s' % x[3], '%30s' % x[4])
            print("Search successful")'''
    except Exception as e:
        print("Error:", e)
        
cart = []

def selectdress(cart):
    num = int(input("Enter the number of products you want to buy: "))
    for i in range(num):
        sdcode = input('Enter the dress code: ')
        if sdcode == 'LD101':
            sdress = ['LD101', 'ZARDOSI LEHENGA', 'LEHENGA', 'RED', 45000]
        elif sdcode == 'LD102':
            sdress = ['LD102', 'SILK SAREE ', 'SAREE', 'PINK', 50000]
        cart.append(sdress)
    print(cart)        
           

        

# jwelleryyyyy
def createtable2():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS jwellery (jcode VARCHAR(10) PRIMARY KEY, jName VARCHAR(50), jtype VARCHAR(10), jcolour CHAR(20), jdescription VARCHAR(500), jprice INT(10), jstock INT(10))")
        mydb.commit()
        print("Table created successfully")
    except Exception as e:
        print("Error creating table:", e)

def addrec():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        n = int(input('Enter the number of records to be added:'))
        for i in range(n):
            jcode = input('Enter jewelry code:')
            jname = input('Enter Name of the jewelry:')
            jtype = input('Enter the type of jewelry:')
            jcolour = input('Enter the colour of the jewelry:')
            jdescription = input('Enter the description of the jewelry:')
            jprice = int(input('Enter the price of the jewelry:'))
            jstock = int(input('Enter the stock of the specific jewelry:'))
            q1 = "INSERT INTO jwellery VALUES ('{}', '{}', '{}', '{}', '{}', {}, {})".format(jcode, jname, jtype, jcolour, jdescription, jprice, jstock)
            mycursor.execute(q1)
            mydb.commit()
        print('Records added successfully')
    except Exception as e:
        print('Error adding records:', e)

def fetchdata():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM jwellery")
        myrecords = mycursor.fetchall()
        
        print(f"%-7s   %-20s   %-12s   %-10s   %-60s   %10s   %-7s" % ('Code', 'Name', 'Type', 'Colour', 'Description', 'Price', 'Stock'))
        
        for x in myrecords:
            code, name, type_, colour, description, price, stock = x
            truncated_description = (description[:57] + '...') if len(description) > 60 else description
            # Adjusted the width of the Stock column to maintain alignment
            print(f"%-7s   %-20s   %-12s   %-10s   %-60s   %10s   %-7s" % (code, name, type_, colour, truncated_description, price, stock))
        
        mycursor.close()
        mydb.close()
    except Exception as e:
        print("Unable to display\n", e)
        

def searchbytype():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        reqrtype = input("Enter the type:")
        query = "SELECT * FROM jwellery WHERE jtype='{}'".format(reqrtype)
        mycursor.execute(query)
        myrecords = mycursor.fetchall()
        if mycursor.rowcount <= 0:
            print("\n## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
            print('{:<10s} {:<15s} {:<10s} {:<10s} {:<60s} {:<10s} {:<10s}'.format('Code', 'Name', 'Type', 'Colour', 'Description', 'Price', 'Stock'))
            for x in myrecords:
                code, name, type_, colour, description, price, stock = x
                truncated_description = (description[:57] + '...') if len(description) > 60 else description
                print('{:<10s} {:<15s} {:<10s} {:<10s} {:<60s} {:<10s} {:<10s}'.format(code, name, type_, colour, truncated_description, str(price), str(stock)))
            print("Search successful")
    except Exception as e:
        print("Error:", e)


def deletebyjcode():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        reqjcode = input("Enter the jewelry code to be deleted:")
        query = "DELETE FROM jwellery WHERE jcode='{}'".format(reqjcode)
        mycursor.execute(query)
        mydb.commit()
        if mycursor.rowcount <= 0:
            print("\n## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
            print("Record deleted successfully")
    except Exception as e:
        print("Error:", e)
def Editbyjcode():
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        reqjcode = input("Enter the jewelry code: ")
        query = "SELECT * FROM jwellery WHERE jcode='{}'".format(reqjcode)
        mycursor.execute(query)
        results = mycursor.fetchall()
        if mycursor.rowcount <= 0:
            print('\n## SORRY! NO MATCHING DETAILS AVAILABLE ##')
        else:
            newname = input("Enter new jewelry name to update (Enter old value if not to update): ")
            newtype = input("Enter new jewelry type to update (Enter old value if not to update): ")
            newcolour = input("Enter new jewelry colour to update (Enter old value if not to update): ")
            newdescription = input("Enter new jewelry description to update (Enter old value if not to update): ")
            newprice = float(input("Enter new jewelry price to update (Enter old value if not to update): "))
            newstock = int(input("Enter new jewelry stock to update (Enter old value if not to update): "))
            query = "UPDATE jwellery SET jName='{}', jtype='{}', jcolour='{}', jdescription='{}', jprice={}, jstock={} WHERE jcode='{}'".format(newname, newtype, newcolour, newdescription, newprice, newstock, reqjcode)
            mycursor.execute(query)
            mydb.commit()
            print("RECORD UPDATED ##")
    except Exception as e:
        print("Error:", e)


def createtable1():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEES(empid VARCHAR(10) primary key, empname VARCHAR(50), emppos VARCHAR(50),empsal INT(10), empcontact VARCHAR(15), empadd VARCHAR(100))")
        mydb.commit()
        print("Table created successfully")
    except Exception as e:
        print("Error creating table:", e)
        
def addemp():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        n = int(input('Enter the number of employee records to be added:'))
        for i in range(n):
            empid = input('Enter employee ID:')
            empname = input('Enter employee name:')
            emppos = input('Enter employee position:')
            empsal = float(input('Enter employee salary:'))
            empcontact = input('Enter employee contact number:')
            empadd = input('Enter employee address:')
            q1 = "INSERT INTO EMPLOYEES VALUES ({}, '{}', '{}', {}, '{}', '{}')".format(empid, empname, emppos, empsal, empcontact, empadd)
            mycursor.execute(q1)
            mydb.commit()
        print('Employee records added successfully')

    except Exception as e:
        print('Error adding employee records:', e)
        
def displayemp():
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM EMPLOYEES")
        myrecords = mycursor.fetchall()

        print('{:<10} {:<25} {:<15} {:<10} {:<12} {:<15}'.format('empid', 'empname', 'emppos', 'empsal', 'empcontact', 'empadd'))
        print('-' * 90)
        for x in myrecords:
            print('{:<10} {:<25} {:<15} {:<10} {:<12} {:<15}'.format(x[0], x[1], x[2], float(x[3]), x[4], x[5]))
    except Exception as e:
        print("Unable to display:", e)



def searchbypos():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        reqpos = input("Enter the employee position:")
        query = "SELECT * FROM EMPLOYEES WHERE emppos='{}'".format(reqpos)
        mycursor.execute(query)
        myrecords = mycursor.fetchall()
        if mycursor.rowcount <= 0:
            print("\n## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
            print('{:<10} {:<25} {:<15} {:<10} {:<12} {:<15}'.format('empid', 'empname', 'emppos', 'empsal', 'empcontact', 'empadd'))  
            print('-' * 90)
            for x in myrecords:
                print('{:<10} {:<25} {:<15} {:<10.2f} {:<12} {:<15}'.format(x[0], x[1], x[2], x[3], x[4], x[5]))  
            print("Search successful")
    except Exception as e:
        print("Error:", e)
     
     
def deletebyempid():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        reqempid = int(input("Enter the employee ID to be deleted:"))
        query = "DELETE FROM EMPLOYEES WHERE empid={}".format(reqempid)
        mycursor.execute(query)
        mydb.commit()
        if mycursor.rowcount <= 0:
            print("\n## SORRY! NO MATCHING DETAILS AVAILABLE ##")
        else:
            print("Record deleted successfully")
    except Exception as e:
        print("Error:", e)

def Editbyempid():
    try:
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        reqempid = int(input("Enter the employee ID: "))
        query = "SELECT * FROM EMPLOYEES WHERE empid={}".format(reqempid)
        mycursor.execute(query)
        results = mycursor.fetchall()
        if mycursor.rowcount <= 0:
            print('\n## SORRY! NO MATCHING DETAILS AVAILABLE ##')
        else:
            newname = input("Enter new employee name to update (Enter old value if not to update): ")
            newcontact = input("Enter new contact number to update (Enter old value if not to update): ")
            newsal = float(input("Enter new salary to update (Enter old value if not to update): "))
            newpos = input("Enter new position to update (Enter old value if not to update): ")
            newadd = input("Enter new address to update (Enter old value if not to update): ")
            query = "UPDATE EMPLOYEES SET empname='{}', empcontact='{}', empsal={}, emppos='{}', empadd='{}' WHERE empid={}".format(newname, newcontact, newsal, newpos, newadd, reqempid)
            mycursor.execute(query)
            mydb.commit()
            print("RECORD UPDATED ##")
    except Exception as e:
        print("Error:", e)
        
cart1=[]
def selectjewellery(cart1):
    num = int(input("Enter the number of products you want to buy: "))
    for i in range(num):
        jcode = input('Enter the jewellery code: ')
        if jcode == 'J1':
            jewels = ['J1', 'RUBY RADIANCE', 'NECKLACE', 'RED','A RED RUBY NECKLACE ADORNED WITH THE FINEST RUBIES.', 90000]
        elif jcode == 'J2':
            jewels = ['J2', 'EMERALD ELEGANCE ', 'NECKLACE', 'GREEN','FINEST EMERALD NECKLACE FOR YOUR FINEST DAY', 88000]
        elif jcode == 'J3':
            jewels = ['J3', 'BRIDAL BLISS ', 'NECKLACE', 'WHITE','BRIDAL NECKLACE ADORNED WITH THE FINEST DIAMONDS', 67000]
        elif jcode == 'J4':
            jewels = ['J4', 'INDIAN SPLENDOR ', 'NECKLACE', 'GOLD','CULTURAL,CEREMONIAL,EXQUISITE GOLD GEMSTONE STUDDED ', 82000]
        elif jcode == 'J5':
            jewels = ['J5', 'ETERNAL SPARKLE ', 'RING', 'WHITE','DIAMONDS RINGS ADORNED WITH DIAMONDS', 22000]
        elif jcode == 'J6':
            jewels = ['J6', 'SHIMMERING HALO ', 'EARRING', 'WHITE','BEAUTIFUL DIAMOND EMBELLISHED EARRINGS', 30000]
        cart1.append(jewels)
    print(cart1)

def print_welcome_message():
    print("*********************************<<R>>********************************".center(50))
    print("*                                                                    *".center(50))
    print("*                      Welcome to Rari Boutique!                     *".center(50))
    print("*                     Discover Elegance and Style                    *".center(50))
    print("*           Step into a world of exquisite fashion and elegance      *".center(50))      
    print("*               at Rari Boutique.  – where fashion meets passion.    *".center(50))
    print("*                Stay Fabulous,The Rari Boutique Team                *" .center(50))
    print("*                                                                    *".center(50))
    print("*********************************<<R>>********************************".center(50))    

    

def print_admin_welcome_message():
    print("********************************* <<R>> *********************************".center(50))
    print("*                                                                       *".center(50))
    print("*                    Welcome to Rari Boutique - Admin Mode\             *".center(50))
    print("*                        Dear Boutique Administrator                    *".center(50))
    print("*                                                                       *".center(50))
    print("********************************* <<R>> *********************************".center(50))    




def create_user_table():
  try:
      mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
      mycursor = mydb.cursor()
      mycursor.execute("""CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50) NOT NULL,password VARCHAR(50) NOT NULL ) """)
      mydb.commit()
      print("")
  except Exception as e:
      print("Error creating table:", e)

def sign_up():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        username = input("Enter your desired username: ")
        password = input("Enter your desired password: ")
        mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mydb.commit()
        print("Sign-up successful!")
    except Exception as e:
        print("Error creating table:", e)


def sign_in():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        mycursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = mycursor.fetchone()
        if user:
           print("Sign-in successful!")
        else:
           print("Invalid username or password.")
    except Exception as e:
        print("Error:", e)


def fetch1data():
    try:
        mydb = mysql.connector.connect(host="localhost", user='root', passwd='efia@123', database='RARIBOUTIQUE')
        mycursor = mydb.cursor()
        mycursor.execute('SELECT jcode, jName, jtype, jcolour, jdescription, jprice FROM jwellery')
        myrecords = mycursor.fetchall()
        
        print(f"%-7s   %-20s   %-12s   %-10s   %-60s   %10s" % ('Code', 'Name', 'Type', 'Colour', 'Description', 'Price'))
        
        for x in myrecords:
            code, name, type_, colour, description, price = x
            truncated_description = (description[:57] + '...') if len(description) > 60 else description
            print(f"%-7s   %-20s   %-12s   %-10s   %-60s   %10s" % (code, name, type_, colour, truncated_description, price))
        
        mycursor.close()
        mydb.close()
    except Exception as e:
        print("Unable to display\n", e)


        

#code for graphh:))    
import matplotlib.pyplot as plt
x = ['LEHENGAS', 'KURTA', 'NECKLACES', 'EARRINGS','RINGS']
y = [22, 3, 9, 4, 1]

plt.bar(x, y)
plt.xlabel("PRODUCT TYPE")
plt.ylabel("STOCK")
plt.title("PRODUCT STOCK")

for i, value in enumerate(y):
    plt.text(i, value, str(value), ha='center', va='bottom')
#codes for images from hereeee:>>
from PIL import Image

def display_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
    except Exception as e:
        print(f"Error: {e}")
image_path = r'C:\Users\user\Downloads\Black and White Luxury Jewellery New Collection Facebook Post.png'


def displayimage2(image11_path):
    try:
        img11 = Image.open(image11_path)
        img11.show()
    except Exception as e:
        print(f"Error: {e}")
image11_path = r"C:\Users\user\Downloads\Black and White Luxury Jewellery New Collection Facebook Post (1).png"

def displayimage3(image3_path):
    try:
        img3 = Image.open(image3_path)
        img3.show()
    except Exception as e:
        print(f"Error: {e}")
image3_path = r"C:\Users\user\Downloads\Purple and Cream Elegant Jewellery New Collection Instagram Story.png"

def displayimage4(image4_path):
    try:
        img4 = Image.open(image4_path)
        img4.show()
    except Exception as e:
        print(f"Error: {e}")
image4_path = r"C:\Users\user\Downloads\boutique (Poster).png"

def shipping():
    print('  SHIPPING ADDRESS ')
    fname=input(" Enter first name: ")
    lname=input("Enter the last name: ")
    address=input(" Enter Address: ")
    pincode=int(input("Enter the pincode: "))
    country=input("Enter the country: ")
    city=input("Enter the city: ")
    phone=int(input("Enter phone: "))
    email=input("Enter the email: ")
    l=[fname,lname,address,pincode,country,city,phone,email]
    print(l)
    print("SHIPPING ADDRESS".center(50, '-'))
    print("First Name:".ljust(15), fname)
    print("Last Name:".ljust(15), lname)
    print("Address:".ljust(15), address)
    print("Pincode:".ljust(15), pincode)
    print("Country:".ljust(15), country)
    print("City:".ljust(15), city)
    print("Phone:".ljust(15), phone)
    print("Email:".ljust(15), email)
    print('-' * 50)


def payment():
    global cart
    total_price = 0
    print("+---------------------- <R> -------------------+".center(50))
    for item in cart:
        print("Product:", item[1]) 
        print("Price:", item[4])     
        total_price += item[4]   
    print("Total Price:", total_price)
    
    sp = 20.00
    print("Shipping price:", sp, "dhs")
    total_price +=sp

    print("Total Price:", total_price)
    print("+---------------------- <R> -------------------+".center(50))
    print("")
    print("+******************** <R> *******************+".center(50))
    print("| Choose payment method                     |".center(50))
    print("|1. Gift card/Coupon                        |".center(50))
    print("|2. Credit/Debit Card                       |".center(50))
    print("|3. Cash on Delivery                        |".center(50))
    print("+******************** <R> *******************+".center(50))
    print('')
    p = int(input("Enter the choice: "))
    if p == 1:
        code=input("Enter a gift card or promotional code")
        print("Processing payment using Gift card/Coupon...")
    elif p == 2:
        cno=int(input("Enter the card number: "))
        expiry=input("Enter expiry month/year: ")
        cvv=int(input('Enter the cvv number : '))
        print("Processing payment using Credit/Debit Card...")
    elif p == 3:
        print("Processing payment using Cash on Delivery...")
    else:
        print("Invalid choice. Payment canceled.")


    
def jpayment():
    global cart1
    total_price = 0
    print("+---------------------- <R> ----------------+".center(50))
    for item in cart1:
        print("Product:", item[1]) 
        print("Price:", item[5])     
        total_price += item[5]   
    print("Total Price:", total_price)
    
    sp = 20.00
    print("Shipping price:", sp, "dhs")
    total_price +=sp

    print("Total Price:", total_price)
    print("+---------------------- <R> ----------------+".center(50))
    print("")
    print("+******************** <R> *******************+".center(50))
    print("| Choose payment method                     |".center(50))
    print("|1. Gift card/Coupon                        |".center(50))
    print("|2. Credit/Debit Card                       |".center(50))
    print("|3. Cash on Delivery                        |".center(50))
    print("+******************** <R> *******************+".center(50))
    print('')
    p = int(input("Enter the choice: "))
    if p == 1:
        code=input("Enter a gift card or promotional code")
        print("Processing payment using Gift card/Coupon...")
    elif p == 2:
        cno=int(input("Enter the card number: "))
        expiry=input("Enter expiry month/year: ")
        cvv=int(input('Enter the cvv number : '))
        print("Processing payment using Credit/Debit Card...")
    elif p == 3:
        print("Processing payment using Cash on Delivery...")
    else:
        print("Invalid choice. Payment canceled.")



'''if __name__ == "__main__":'''
def main():
    admin_username = "rari"
    admin_password = "2006"
        

    while True:
        print("*" * 50)
        print("+--------- <R> -----------+".center(50))
        print("|                         |".center(50))
        print("|      RARI Boutique      |".center(50))
        print("|                         |".center(50))
        print("|      DESIGNER WEAR      |".center(50))
        print("|           AND           |".center(50))
        print("|        JEWELLERY        |".center(50))
        print("|                         |".center(50))
        print("|                         |".center(50))
        print("+----------<R>------------+".center(50))
        print("")
        print("Welcome to Rari Boutique!".center(50))
        print("")
        print("")
        print("╔+---------------------- <:<R>:> -----------------------+╗".center(50))
        print("║                  <<<CHOOSE A MODE>>>                   ║".center(50))
        print("║                                                        ║".center(50))
        print("║    1.ADMIN MODE    2.CUSTOMER MODE     3.EXIT          ║".center(50))
        print("║                                                        ║".center(50))
        print("║+---------------------- <:<R>:> -----------------------+║".center(50))
        print("")
        mode_choice = input("ENTER YOUR DESIRED CHOICE: ")
        print("")



        if mode_choice == '1':
            entered_username = input("Enter admin username: ")
            entered_password = input("Enter admin password: ")
            
            if entered_username == admin_username and entered_password == admin_password:
                admin_mode()
            else:
                print("Invalid admin credentials. Access denied.")
                break
        elif mode_choice == '2':
            customer_mode()
        elif mode_choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            


def admin_mode():
    print("")
    print("")
    print_admin_welcome_message()
    while True:
        print("")
        print("")
        print("+~~~~~~~~ <:<R>:> ~~~~~~~~~+".center(50))
        print("|                          |".center(50))
        print("|         Admin Mode       |".center(50))
        print("|         1.DRESSES        |".center(50))
        print("|         2.JEWELLERY      |".center(50))
        print("|         3.EMPLOYEES      |".center(50))
        print("|         4.EXIT           |".center(50))
        print("|                          |".center(50))
        print("+~~~~~~~~ <:<R>:> ~~~~~~~~~+".center(50))
        print("")
        ch = int(input('ENTER YOUR DESIRED CHOICE:'))
        print("")
        print("")
        if ch==1:
           while True:
            print("+~~~~~~~~~~~~~ <:<*>:> ~~~~~~~~~~~~~+".center(50))
            print("|                                   |".center(50))
            print("|       1. CREATE dress TABLE       |".center(50))
            print("|       2. ADD dress                |".center(50))
            print("|       3. DISPLAY dress            |".center(50))
            print("|       4. UPDATE RECORD            |".center(50))
            print("|       5. DELETE RECORD            |".center(50))
            print("|       6. SEARCH DRESS TYPE        |".center(50))
            print("|                                   |".center(50))
            print("+~~~~~~~~~~~~~~ <:<*>:> ~~~~~~~~~~~~+".center(50))
            print("")
            dch=int(input('ENTER YOUR DESIRED CHOICE:'))
            if dch==1:
                createdtable()
            elif dch==2:
                addrecord()
            elif dch==3:
                fetchdatad()
            elif dch==4:
                editbydno()
            elif dch==5:
                deletebydno()
            elif dch==6:
                searchdbytype()
            else:
                break
                
        elif ch==2:
           while True:
            print("")
            print("")
            print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+".center(50))
            print("|                                              |".center(50))
            print("|            1. Create Jewelry Table           |".center(50))
            print("|            2. Add Jewelry                    |".center(50)) 
            print("|            3. Display Jewelry                |".center(50))
            print("|            4. Search by Type                 |".center(50))
            print("|            5. Delete by Jewelry Code         |".center(50))
            print("|            6. Update by Jewelry Code         |".center(50))
            print("|            7. view stock graph               |".center(50))
            print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+".center(50))
            print("")
            jch=int(input('ENTER YOUR DESIRED CHOICE:'))
            if jch==1:
                createtable2() 
            elif jch==2:
                addrec()
            elif jch==3:
                fetchdata()
            elif jch==4:
                searchbytype()
            elif jch==5:
                deletebyjcode()
            elif jch==6:
                Editbyjcode()
            elif jch==7:
                plt.show()
            else:
                break
                
        elif ch==3:
           while True:
            print("")
            print("")
            print("+~~~~~~~~~~~~~~~~~~~ <:<*>:> ~~~~~~~~~~~~~~~~~~+".center(50))
            print("|                                              |".center(50))
            print("|           1. Create Employee Table           |".center(50))
            print("|           2. Add Employee                    |".center(50))
            print("|           3. Display Employee                |".center(50))
            print("|           4. Search by Position              |".center(50))
            print("|           5. Delete by Employee ID           |".center(50))
            print("|           6. Update by Employee ID           |".center(50))
            print("|                                              |".center(50))
            print("+~~~~~~~~~~~~~~~~~~~ <:<*>:> ~~~~~~~~~~~~~~~~~~+".center(50))
            print("")
            ech=int(input('ENTER YOUR DESIRED CHOICE:'))
            if ech==1:
                createtable1() 
            elif ech==2:
                addemp()
            elif ech==3:
                displayemp()
            elif ech==4:
                searchbypos()
            elif ech==5:
                deletebyempid()
            elif ech==6:
                Editbyempid()
            else:
                 break
        else:
              break
        
def customer_mode():
    print("")
    print("")
    print_welcome_message()
    print("")
    print("")
    display_image(image_path)

    create_user_table()
    while True:
        print("")
        print("")
        print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+".center(50))
        print("|        ---------------*--------------        |".center(50))
        print("|                  Customer Mode               |".center(50))
        print("|                Choose an option:             |".center(50))
        print("|                  1. Sign Up                  |".center(50))
        print("|                  2. Sign In                  |".center(50))
        print("|        ---------------*--------------        |".center(50))
        print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+".center(50))
        print("")
        ch = int(input('ENTER YOUR DESIRED CHOICE:'))
        print("")
        if ch == 1:
            sign_up()
        elif ch == 2:
           sign_in()
           while True:
            print("")
            print("")
            print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+".center(50))
            print("|        ---------------*--------------        |".center(50))
            print('|           1. Shop for WOMEN DRESSES          |'.center(50))
            print('|           2. Shop for Jewelry                |'.center(50))
            print("|           3.Exit                             |".center(50))
            print("|        ---------------*--------------        |".center(50))
            print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+".center(50))
            print("")
            choice = int(input("ENTER YOUR DESIRED CHOICE: "))
            
            if choice == 1:
               while True:
                print("")
                print("")
                print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+".center(50))
                print("|        ---------------*--------------        |".center(50))
                print("|           1. Display ALL DRESSES             |".center(50))
                print("|           2. Display Dresses by type         |".center(50))
                print("|           3. Select dress                    |".center(50))
                print("|           4.Generate bill for Dress          |".center(50))
                print("|        ---------------*--------------        |".center(50))
                print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+".center(50))
                print("")
                CH = int(input('ENTER YOUR DESIRED CHOICE:'))
                print("")
                if CH == 1:
                    fetchdatad()
                    displayimage4(image4_path)
                elif CH == 2:
                    searchdbytype()
                elif CH==3:
                    selectdress(cart)
                elif CH==4:
                   while True:
                    print("")
                    print("")
                    print("+~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~+".center(50))
                    print('|1. Shipping details                   |'.center(50))
                    print('|2. payment                            |'.center(50))
                    print('|3. exit                               |'.center(50))
                    print("+~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~+".center(50))
                    print("")
                    cho=int(input("Enter the numbers"))
                    if cho==1:
                        shipping()
                    elif cho==2:
                         payment()
                    elif cho==3:
                        break
                    
                
                
            elif choice == 2:
               while True:
                print("")
                print("")
                print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+".center(50))
                print("|        ---------------*--------------        |".center(50))
                print("|           1. Display ALL JEWELLERY           |".center(50))
                print("|           2. Display Jewellry by Type        |".center(50))
                print("|           3. Select Jewellery                |".center(50))
                print("|           4.Generate bill for Jewellery      |".center(50))
                print("|        ---------------*--------------        |".center(50))
                print("+~~~~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~~~~~~+")
                print("")
                CH = int(input('ENTER YOUR DESIRED CHOICE:'))
                print("")
                if CH == 1:
                    fetch1data()
                    displayimage2(image11_path)
                    displayimage3(image3_path)
                elif CH == 2:
                    searchbytype()
                elif CH == 3:
                    selectjewellery(cart1)
                elif CH == 4:
                   while True:
                    print("")
                    print("")
                    print("+~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~+".center(50))
                    print('|1. Shipping details                   |'.center(50))
                    print('|2. payment                            |'.center(50))
                    print('|3. exit                               |'.center(50))
                    print("+~~~~~~~~~~~~~~~~ <:<>:> ~~~~~~~~~~~~~~+".center(50))
                    print("")
                    cho=int(input("Enter the numbers"))
                    if cho==1:
                        shipping()
                    elif cho==2:
                         jpayment()
                    elif cho==3:
                        break
                    
                else:
                    break
                
                    
                
                          
                
main()
