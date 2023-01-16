import tkinter as tk
import sqlite3

# Buat koneksi ke database
conn = sqlite3.connect('db_uas_pbo.db')
cursor = conn.cursor()

# Eksekusi query untuk mengambil data mahasiswa
query = 'SELECT nim, nama, jenis_kelamin FROM mahasiswa'
cursor.execute(query)
data = cursor.fetchall()

# Buat GUI
root = tk.Tk()
root.title('Data Mahasiswa')

# Buat tabel
table = tk.Treeview(root, columns=(
    'nim', 'nama', 'jenis_kelamin'), show='headings')
table.heading('nim', text='NIM')
table.heading('nama', text='Nama')
table.heading('jenis_kelamin', text='Jenis Kelamin')

# Tambahkan data ke tabel
for item in data:
    table.insert('', 'end', values=item)

# Tampilkan tabel
table.pack()
root.mainloop()

# Tutup koneksi ke database
conn.close()
