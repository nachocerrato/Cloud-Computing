import pyodbc
print("Buscando departamentos")

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"

cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL server}; SERVER="+servidor+
                "; DATABASE=" +bbdd+ "; UID=" +usuario+ "; PWD=" + password)

conexion = pyodbc.connect(cadenaconexion)

numero = input()
sql = "select dept_no, dnombre, loc from dept where dept_no = 10" + numero
cursor = conexion.execute(sql)
row = cursor.fetchone()
print(row)
if(row == "None"):
    print("No existe el departamento.")
else:
    print(row.dnombre + ", " + row.Loc)

cursor.close()
conexion.close()
print("Fin de programa")