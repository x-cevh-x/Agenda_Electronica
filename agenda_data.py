from data_source import Data_Source


class data_agenda:

    def obtener_contactos(self):
        contacto = Data_Source().listar_contactos()

        print("\n****** Lista de Contactos ******\n")
        print("Nombre\t|\tApellido\t|\tTelefono")
        print("____________________________________")

        for dato in contacto:
            print(f"{dato.name}\t\t{dato.last_name}\t\t{dato.tel}")
        print("____________________________________")
        print(f"Numero de contactos registrados:{len(contacto)}")

    def crear_contacto(self, nombre, apellido, telefono) -> str:
        data_source = Data_Source()
        return data_source.agregar_contacto(nombre, apellido, telefono)

    def buscar_contacto(self, dato):

        busqueda = Data_Source().buscar_contacto(dato)
        if (len(busqueda) > 0):
            print("\n****** Buscar Contacto ******\n")
            print("N° Lista\t|\tNombre\t|\tApellido\t|\tTelefono")
            print("_________________________________________________________")
            for dato in busqueda:
                print(f"\t{dato.id}\t\t\t{dato.name}\t\t{dato.last_name}\t\t\t{dato.tel}")
            print("_________________________________________________________")
            print(f"Numeros de contactos encontrado {len(busqueda)}")
        else:
            print("No se encontro contacto...")

    def selecionar_contacto(self, id):
        busqueda = Data_Source().seleccionar_contacto(id)

        print("N° Lista\t|\tNombre\t|\tApellido\t|\tTelefono")
        print("_________________________________________________________")
        for dato in busqueda:
            print(f"\t{dato.id}\t\t\t{dato.name}\t\t{dato.last_name}\t\t\t{dato.tel}")
        print("_________________________________________________________")

    def editar_contacto(self, id, nombre = None, apellido = None, telefono = None):
        print("\n****** Contacto a Editar ******\n")
        contacto = Data_Source().seleccionar_contacto(id)
        update = Data_Source()
        for dato in contacto:

            if nombre == "" or apellido == "" or telefono == "":
                if len(nombre) == 0:
                    nombre = dato.name

                if len(apellido) == 0:
                    apellido = dato.last_name

                if len(telefono) == 0:
                    telefono = dato.tel

                print(update.actualizar_contacto(id, nombre, apellido, telefono))

            else:
                print(update.actualizar_contacto(id, nombre, apellido, telefono))

    def eliminar_contacto(self, id):

        contacto = Data_Source()
        print(contacto.eliminar_contacto(id))






if __name__ == '__main__':
    test = data_agenda()
    test.eliminar_contacto(7)
