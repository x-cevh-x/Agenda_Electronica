import ResourceBundle
import mysql.connector


class Conn:
    __cf = ResourceBundle.get_bundle("config")
    __host = __cf.get("host")
    __user = __cf.get("user")
    __pass = __cf.get("password")
    __db = __cf.get("database")

    def conn(self):
        try:
            cnn = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__pass, database=self.__db)
            return cnn
        except Exception as e:
            print(f"Error: No se puede conectar a la Base de datos\n {e}")

    def insertdatos(self, name, lastname, tel) -> str:
        cnn = self.conn()
        query = cnn.cursor()
        sql = "INSERT INTO contacto (nombre, apellido, numero_telefono) VALUES (%s, %s, %s)"
        datos = (name, lastname, tel)
        query.execute(sql, datos)
        cnn.commit()
        if query.rowcount > 0:
            return "Contacto agregado"
        else:
            return "Error no se guardo el contacto"

    def selectDatos(self):
        cnn = self.conn()
        query = cnn.cursor()
        query.execute("SELECT nombre, apellido, numero_telefono FROM contacto")
        rs = query.fetchall()
        return rs

    def buscarDatos(self, name) -> list:
        cnn = self.conn()
        query = cnn.cursor()
        sql = "SELECT * FROM contacto WHERE nombre LIKE '%{}%' OR apellido LIKE '%{}%'".format(name, name)
        query.execute(sql)
        rs = query.fetchall()
        return rs

    def editarDatos(self, id, name, last_name, tel):
        try:

            cnn = self.conn()
            query = cnn.cursor()
            sql = "UPDATE contacto SET nombre = '{}', apellido = '{}', numero_telefono = '{}' WHERE id_contacto = {} ".format(name, last_name, tel, id)
            query.execute(sql)
            cnn.commit()
            if query.rowcount > 0:
                return "**** Contacto actualizado ****"
            else:
                return "!Error¡: No se pudo actualizar el contacto"
        except Exception as e:
            print(f"Error:{e}")

    def selectUnicoDato(self, id):
        cnn = self.conn()
        query = cnn.cursor()
        sql = "SELECT * FROM contacto where id_contacto = {}".format(id)
        query.execute(sql)
        return query.fetchall()

    def eliminarContacto(self, id):
        try:
            cnn = self.conn()
            query = cnn.cursor()
            sql = "DELETE FROM contacto WHERE id_contacto = {}".format(id)
            query.execute(sql)
            if query.rowcount > 0:
                return "Contacto Eliminado!"
            else:
                return "Error!: No se pudo eliminar el contacto..."
        except Exception as e:
            print(f"Erro:{e}")
#'''
if __name__ == '__main__':
    conn = Conn()
    #print(conn.editarDatos(5,"Daniel", "Valencia", "3152214227"))
    print(conn.selectUnicoDato(6))
#'''
