import mysql.connector

# Kết nối tới MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",

  password="12345678",
  database="mydatabase"
)

# Tạo một đối tượng cursor để thực hiện truy vấn SQL
mycursor = mydb.cursor()

# Tạo bảng trong cơ sở dữ liệu
# mycursor.execute("CREATE TABLE tasks (idTask INT AUTO_INCREMENT PRIMARY KEY NOT NULL, nameTask VARCHAR(45) NOT NULL, descriptions VARCHAR(255), estimate INT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, progress VARCHAR(45) NOT NULL, Comments VARCHAR(255)),")

# # Chèn dữ liệu vào bảng
# sql = "INSERT INTO persons (name, phone, userName, password) VALUES (%s, %s,%s,%s)"
# val = ("Huyen", "9911652", "huyennn", "12345678")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)

# # Lấy dữ liệu từ bảng
# mycursor.execute("SELECT * FROM persons")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

mydb.close()