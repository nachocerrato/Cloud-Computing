import pyodbc

print("Primera consulta SQL Server")
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
#cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL server}; SERVER="+servidor+
#                "; DATABASE=" +bbdd+ "; UID=" +usuario+ "; PWD=" + password)

#conexion con seguridad windows
cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL server}; SERVER="+servidor+
                "; DATABASE=" +bbdd+ "; Trusted_connection=yes")

try:
    print("Intentando conectar...")
    pyodbc.connect(cadenaconexion)
    print("Conectado!!!")
except:
    print("Pinta mal la cosa")
print("Fin del programa")