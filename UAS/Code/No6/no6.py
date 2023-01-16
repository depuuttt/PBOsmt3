import mysql.connector

# koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_uas_pbo"
)

# membuat cursor
cursor = db.cursor()

# menjalankan query SELECT
cursor.execute("SELECT * FROM mahasiswa")

# menampilkan hasil query
result = cursor.fetchall()
for data in result:
    print(data)

# menutup koneksi
cursor.close()
db.close()
