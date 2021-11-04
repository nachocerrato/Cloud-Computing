import pyodbc

print("Primera consulta SQL Server")
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"

cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL server}; SERVER="+servidor+
                "; DATABASE=" +bbdd+ "; UID=" +usuario+ "; PWD=" + password)

#conexion con seguridad windows
#cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL server}; SERVER="+servidor+
#                "; DATABASE=" +bbdd+ "; Trusted_connection=yes")
print("Intentando conectar...")
conexion = pyodbc.connect(cadenaconexion)
print("Conectado!!!")
#cursor se crea con una conexión abierta
cursor = conexion.cursor()
sql = "select * from dept"
cursor.execute(sql)
row = cursor.fetchone()
print(row)
conexion.close()
print("Fin del programa")

