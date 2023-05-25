from sqlite3 import Error
import sqlite3

def Crear_Coneccion():
    try:
        conn= sqlite3.connect("DataBase/BaseDeDatos.db")
        return conn
    except Error as e:
        print ("Error de coneccion del db: ",str(e))

def insertar(data):
    conn=Crear_Coneccion()
    sql = """INSERT INTO Usuario (Nombre, Usuario, Contra, Tipo) VALUES(?, ?, ?, ?)"""
    try:
        cur=conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        return True, cur.lastrowid
    except Error as e:
        print("ERROR funcion instertar datos ", str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def BuscarUser(data):
    conn = Crear_Coneccion()
    sql = f"SELECT Usuario.* FROM Usuario WHERE Usuario = '{data}'"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        user=cur.fetchone()
        return user
    except Error as e:
        print("Error al seleccion el usuario: ",str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
    
def BuscarVendedor(data):
    conn = Crear_Coneccion()
    sql = f"SELECT Usuario.* FROM Usuario WHERE Tipo = '{data}'"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        user=cur.fetchone()
        return user
    except Error as e:
        print("Error al Buscar User Vendedor: ",str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def Ventas():
    conn =Crear_Coneccion()
    sql = f"SELECT Ventas.* FROM Ventas"
    try:
        cur =conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
    except Error as e:
        print("Error al buscar ventas")
    finally:
        if conn:
            cur.close()
            conn.close()

def insertarVenta(data):
    conn=Crear_Coneccion()
    sql = """INSERT INTO Ventas (Usuario, NombreProducto, TipoDeProducto, Precio, Cantidad) 
                VALUES(?,?,?,?,?)"""
    try:
        cur=conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        return True, cur.lastrowid
    except Error as e:
        print("ERROR", str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insertarCompra(data):
    conn=Crear_Coneccion()
    sql = """INSERT INTO Compras (Usuario, NombreProducto, TipoDeProducto, Precio, Fecha) 
                VALUES(?,?,?,?,?)"""
    try:
        cur=conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        return True
    except Error as e:
        print("ERROR ", str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def BuscarProducto(datoBusqueda,tipo):
    conn=Crear_Coneccion()
    if tipo =="Vendedor":
        sql = f"SELECT * FROM Ventas WHERE Usuario LIKE '%{datoBusqueda}%'"
    elif tipo == "Producto":
        sql = f"SELECT * FROM Ventas WHERE NombreProducto LIKE '%{datoBusqueda}%'"
    elif tipo == "Tipo":
        sql = f"SELECT * FROM Ventas WHERE TipoDeProducto LIKE '%{datoBusqueda}%'"
    elif tipo == "Precio":
        sql = f"SELECT * FROM Ventas WHERE Precio LIKE '%{datoBusqueda}%'"
    elif tipo == "Cantidad":
        sql = f"SELECT * FROM Ventas WHERE Cantidad LIKE '%{datoBusqueda}%'"

    try:
        cur= conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
    except Error as e:
        print("Error: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def BuscarCompras(User):
    conn=Crear_Coneccion()        
    sql = f"SELECT * FROM Compras WHERE Usuario LIKE '%{User}%'"
    try:
        cur= conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
    except Error as e:
        print("Error: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def EliminarVenta(_id):
    conn=Crear_Coneccion()
    sql =f"DELETE FROM Ventas WHERE ID_venta = {_id}"
    try: 
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Venta Eliminado")
        return True
    except Error as e:
        print("Error: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def Actuali(_user, info):
    conn=Crear_Coneccion()
    sql = f""" UPDATE Usuario SET 
                            Nombre= ?,
                            Usuario= ?,
                            Contra= ?,
                            Tipo = ?
                WHERE Usuario = '{_user}'
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, info)
        conn.commit()        
        return True
    except Error as e:
        print("Error: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def EnviarMen(data):
    conn=Crear_Coneccion()
    sql = """INSERT INTO Comentario (User,Mensaje,Product)VALUES(?, ?, ?)"""
    try:
        cur=conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        return True
    except Error as e:
        print("ERROR funcion instertar datos ", str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def BuscarMensajeProduc(Valor):
    conn = Crear_Coneccion()
    sql = f"SELECT Comentario.* FROM Comentario WHERE Product = '{Valor}'"
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        Mens=cur.fetchall()
        return Mens
    except Error as e:
        print("Error al Buscar Mensaje: ",str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
 
