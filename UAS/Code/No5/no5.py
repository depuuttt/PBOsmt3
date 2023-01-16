import tkinter as tk


def tampil_pesan():
    label.config(text="Aldi Maulana Iqbal - 20210801222")


root = tk.Tk()
root.title("UAS PBO Nomor 5")

label = tk.Label(root, text="Press the button below to see this user profile!")
label.pack()

tombol = tk.Button(root, text="Show Profile", command=tampil_pesan)
tombol.pack()

root.mainloop()
