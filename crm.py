from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import csv

root = Tk()
root.title("Database")
root.iconbitmap('C:/Users/Ghanendra/Desktop/gk.ico')
root.geometry("400x600")

 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tinu@2001",
    database="gkc",
 )


#create cursor and initialise
my_cursor = mydb.cursor()


#create database
#my_cursor.execute("CREATE DATABASE gkc")


#test to see if database is created
#my_cursor.execute("SHOW DATABASES")


#crete table
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255), \
           last_name VARCHAR(255), \
           zipcode int(10), \
           price_paid DECIMAL(10, 2), \
           user_id INT AUTO_INCREMENT PRIMARY KEY) ")
'''
#ALTER  table
my_cursor.execute("ALTER TABLE customers ADD  (email VARCHAR(255), \
        address_1 VARCHAR(255), \
        address_2 VARCHAR(255), \
        city VARCHAR(50), \
        state VARCHAR(50), \
        country VARCHAR(255), \
        phone VARCHAR(255), \
        payment_method VARCHAR(50), \
        discount_code VARCHAR(255)) ")
'''
#clear function
def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address_1_box.delete(0, END)
    address_2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
   # user_id_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

#add function
def add_customer():
    sql_command = "INSERT INTO customers (first_name, Last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address_1_box.get(), address_2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
    my_cursor.execute(sql_command, values)

    # commit the change to the database
    mydb.commit()
    #clear fields
    clear_fields()

# write to csv
def write_to_csv(result):
    with open('customers.csv', 'a', newline="") as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)


#list customers
def list_customers():
    list_customers_query = Tk()
    list_customers_query.title("List All Customers")
    list_customers_query.iconbitmap('C:/Users/Ghanendra/Desktop/gk.ico')
    list_customers_query.geometry("800x600")
# QUERY THE DATABASE
    my_cursor.execute("SELECT * FROM customers")
    result = my_cursor.fetchall()
    for index, x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customers_query, text=y)
            lookup_label.grid(row=index, column=num)
            num +=1

    csv_button = Button(list_customers_query, text="Save to Exel", command=lambda : write_to_csv(result))
    csv_button.grid(row=index+1, column=0)
#show table
#my_cursor.execute("SELECT * FROM customers")
#print(my_cursor.description)

#for thing in my_cursor.description:
#    print(thing)

#create label
title_label = Label(root, text="Customer Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady="10")

#create main frame
first_name_label = Label(root, text="First Name").grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Last Name").grid(row=2, column=0, sticky=W, padx=10)
zipcode_label = Label(root, text="Zipcode").grid(row=7, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(row=14, column=0, sticky=W, padx=10)
#user_id_label = Label(root, text="User ID").grid(row=11, column=0, sticky=W, padx=10)
email_label = Label(root, text="Email").grid(row=10, column=0, sticky=W, padx=10)
address_1_label = Label(root, text="Address 1").grid(row=3, column=0, sticky=W, padx=10)
address_2_label = Label(root, text="Address 2").grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text="state").grid(row=6, column=0, sticky=W, padx=10)
country_label = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text="Phone").grid(row=9, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text="Payment Method").grid(row=12, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code").grid(row=13, column=0, sticky=W, padx=10)

#entry box
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1)

last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address_1_box = Entry(root)
address_1_box.grid(row=3, column=1, pady=5)

address_2_box = Entry(root)
address_2_box.grid(row=4, column=1, pady=5)

city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)

#user_id_box = Entry(root)
#user_id_box.grid(row=10, column=1, pady=5)

payment_method_box = Entry(root)
payment_method_box.grid(row=12, column=1, pady=5)

discount_code_box = Entry(root)
discount_code_box.grid(row=13, column=1, pady=5)

price_paid_box = Entry(root)
price_paid_box.grid(row=14, column=1, pady=5)

#add buttons
add_customer_button = Button(root,text="Add Customer to Database", command=add_customer)
add_customer_button.grid(row=15, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=15, column=1, padx=10, pady=10)

# list custoomers
list_customers_button = Button(root, text="List Customers", command=list_customers)
list_customers_button.grid(row=16, column=0, sticky=W, padx=10)

root.mainloop()