import time

from agenda_data import data_agenda

def eliminar_contacto(id):
    agenda = data_agenda()
    print("\n****** Contacto a Eliminar ******\n")
    agenda.selecionar_contacto(id)
    while True:

        try:
            rs = input('Seguro de eliminar al contacto? s/n: ')
            if rs == 's':
                print("Eliminando Contacto...")
                time.sleep(3)
                agenda.eliminar_contacto(id)
                break
            elif rs == 'n':
                print("Saliendo a menu principal...")
                time.sleep(3)
                break
        except Exception as e:
            print(f"Error!: Opcion incorrecta\n{e}")

def editar_contacto(id):
    agenda = data_agenda()
    agenda.selecionar_contacto(id)
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Telefono: ")
    agenda.editar_contacto(id, nombre, apellido, telefono)
    print("")

def busqueda_contacto(dato) :
    agenda = data_agenda()
    agenda.buscar_contacto(dato)
    print("\n")

def lista_contactos():
    agenda = data_agenda()
    agenda.obtener_contactos()
    print("\n")


def nuevo_contacto():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("telefono: ")
    agenda = data_agenda()
    print(agenda.crear_contacto(nombre, apellido, telefono))
    print("\n")



if __name__ == '__main__':

    while True:
        try:
            print("1- Crear contacto\n"
                  "2- Ver contactos\n"
                  "0- Salir")
            opc = int(input("Ingresa una opcion:"))
            match opc:
                case 1:
                    nuevo_contacto()
                case 2:
                    lista_contactos()
                    print("3- Buscar Contacto\n"
                          "0- Salir al menu principal\n")
                    opc = int(input("Ingresa Opcion: "))
                    match opc:
                        case 3:
                            print("Buscar contacto por nombre o apellido")
                            valor = input("Ingrese contacto a buscar: ")
                            busqueda_contacto(valor)
                            print("Para editar o eliminar un contacto ten encuenta el numero de la lista del contacto...")
                            print("")
                            print("1- Editar Contacto\n2- Eliminar Contacto")
                            opc = int(input("Accion a realizar: "))
                            match opc:
                                case 1:
                                    id = int(input("ingrese el numero de lista del contacto a editar: "))
                                    editar_contacto(id)
                                case 2:
                                    id = int(input("ingrese el numero de lista del contacto a eliminar: "))
                                    eliminar_contacto(id)
                case 0:
                    break
        except Exception as e:
            print(f"Error la opcion que ingresastes es incorrecta...\n{e}")
