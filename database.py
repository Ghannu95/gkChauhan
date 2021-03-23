from tkinter import *
from PIL import ImageTk, Image
from tkinter import  messagebox
import sqlite3


root = Tk()
root.title("Ghanendra... ")
root.iconbitmap('C:/Users/Ghanendra/Desktop/gk.ico')


#create database or connect to one
conn = sqlite3.connect('address_book.db')

#create cursor
c = conn.cursor()

#create table

#c.execute(""" CREATE TABLE addresses(
 #   first_name text,
  #  last_name text,
   # address text,
    #city text,
    #state tex,
    #zipcode integer)
    #""")

# create update button
def update():
    # create database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    record_id = s_box.get()
    c.execute("""UPDATE addresses SET
         first_name = :f_name, 
         last_name = :l_name,
         address = :address,
         city = :city,
         state = :state,
         zipcode = :zipcode

         WHERE oid = :oid""",
        {
            'f_name': f_name_editor.get(),
            'l_name': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            'oid': record_id
              })

    # commit change
    conn.commit()
    # close connection
    conn.close()



#edit function
def edit():
    global editor
    editor = Tk()
    editor.title("Update Records. ")
    editor.iconbitmap('C:/Users/Ghanendra/Desktop/gk.ico')
    editor.geometry("400x300")
    # create database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    record_id = s_box.get()
    # query database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()


  #  print_records = ''
    #for record in records:
    #    print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"  # ammend this thing according to our needs

    #make global variable
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)


    # create text boxes
    f_name_lbl = Label(editor, text="First Name")
    f_name_lbl.grid(row=0, column=0, pady=(10, 0))
    l_name_lbl = Label(editor, text="Last Name")
    l_name_lbl.grid(row=1, column=0)
    address_lbl = Label(editor, text="Address")
    address_lbl.grid(row=2, column=0)
    city_lbl = Label(editor, text="City")
    city_lbl.grid(row=3, column=0)
    state_lbl = Label(editor, text="State")
    state_lbl.grid(row=4, column=0)
    zipcode_lbl = Label(editor, text="Zipcode")
    zipcode_lbl.grid(row=5, column=0)
    # loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # create submit button
    b = Button(editor, text="Submit", command=update)
    b.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)



#delete record
def delete():
    # create database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    #delete a rcord
    c.execute("DELETE from addresses WHERE oid= " + s_box.get())

    # commit change
    conn.commit()
    # close connection
    conn.close()


#create submit function
def submit():
    # create database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    #insert data
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city':  city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
 # commit change
    conn.commit()
   # close connection
    conn.close()
    #clear text boxes
    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    # create database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()
    #query database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"#ammend this thing according to our needs

    q_lbl = Label(root, text=print_records)
    q_lbl.grid(row=12, column=0, columnspan=2)

    # commit change
    conn.commit()
    # close connection
    conn.close()



f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20,pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
s_box = Entry(root, width=30)
s_box.grid(row=9, column=1, pady=5)

#create text boxes
f_name_lbl = Label(root, text="First Name")
f_name_lbl.grid(row=0, column=0, pady=(10,0))
l_name_lbl = Label(root, text="Last Name")
l_name_lbl.grid(row=1, column=0)
address_lbl = Label(root, text="Address")
address_lbl.grid(row=2, column=0)
city_lbl = Label(root, text="City")
city_lbl.grid(row=3, column=0)
state_lbl = Label(root, text="State")
state_lbl.grid(row=4, column=0)
zipcode_lbl = Label(root, text="Zipcode")
zipcode_lbl.grid(row=5, column=0)
s_box_lbl = Label(root, text="Selete ID")
s_box_lbl.grid(row=9, column=0, pady=5)


#create submit button
b = Button(root, text="Add record to database", command=submit)
b.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# create a query button
q_button = Button(root, text="Show record", command=query)
q_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=130)

# DELETE BUTTON
d_button = Button(root, text="Delete record", command=delete)
d_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=128)

#Update record
edit_button = Button(root, text="Edit record", command=edit)
edit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=134)

#commit change
conn.commit()

#close connection
conn.close()



root.mainloop()