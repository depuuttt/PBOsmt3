import tkinter as tk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_uas_pbo"
)

cursor = db.cursor()
query = "SELECT * FROM mahasiswa"
cursor.execute(query)
mahasiswa = cursor.fetchall()


def create():
    print("Create selected")


def read():
    print("Read selected")


def update():
    print("Update selected")


def delete():
    print("Delete selected")


root = tk.Tk()
root.title("UAS PBO")
root.geometry("640x320")

l = tk.Label(root, text="Sistem Informasi Mahasiswa")
l.config(font=("Roboto", 14))
l.pack()

m = tk.Label(root, text="Oleh Aldi Maulana Iqbal (20210801222)")
m.config(font=("Roboto", 12), fg="#808080")
m.pack(padx=5, pady=5)

read_button = tk.Button(root, text="Show Data",
                        command=read, width=15, height=1)
read_button.pack(padx=5, pady=5)

create_button = tk.Button(root, text="Input Data",
                          command=create, width=15, height=1)
create_button.pack(padx=5, pady=5)

update_button = tk.Button(root, text="Edit Data",
                          command=update, width=15, height=1)
update_button.pack(padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Data",
                          command=delete, width=15, height=1)
delete_button.pack(padx=5, pady=5)

root.mainloop()
