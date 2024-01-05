from Agenda import Agenda
from conn import Conn


class Data_Source:

    def listar_contactos(self):
        rs = Conn().selectDatos()
        lista = []
        for i in rs:
            lista.append(Agenda(id=0,name=i[0], last_name = i[1], tel=i[2]))
        return lista

    def agregar_contacto(self, name, last_name, tel):
        contacto = Conn()
        rs = contacto.insertdatos(name, last_name, tel)
        return rs

    def buscar_contacto(self, dato):
        rs = Conn()
        lista = []
        for i in rs.buscarDatos(dato):
            lista.append(Agenda(i[0], i[1], i[2], i[3]))
        return lista

    def seleccionar_contacto(self, id):
        rs = Conn()
        lista = []
        for i in rs.selectUnicoDato(id):
            lista.append(Agenda(i[0], i[1], i[2], i[3]))
        return lista

    def actualizar_contacto(self, id, name, last_name, tel):
        contacto = Conn()
        rs = contacto.editarDatos(id, name, last_name, tel)
        return rs

    def eliminar_contacto(self, id):
        contacto = Conn()
        rs = contacto.eliminarContacto(id)
        return rs

#'''
if __name__ == '__main__':
    conn = Data_Source()
    print(conn.actualizar_contacto(5,"Dilan","Angulo", "3185554441"))
#'''
