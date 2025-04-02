clientes = {
    456:{
        "NOMBRE" : "juan",
        "APELLIDO" : "pere",
        "CORREO" : "juan@gmail.com",
        "TELEFONO" : "32445859",
        "DIRECCION" : "calle falsa 456",
        "PREFERENCIAL" : True
    }
}

def obtener_opcion():
    while True: 
        try:
            opcion = int(input('Seleccione una opción: '))
            if 1 <= opcion <= 5:
                return opcion
            print('Por favor, ingrese una opción válida (1-5).')
        except ValueError:
            print('Error: Debe ingresar un número. Intente nuevamente.')

def pausar():
    input("\nPresione Enter para continuar...")


def mostrar_menu():
    print('✨✨ ------------------------------✨✨')
    print('--- Bienvenido al registro de notas ---')
    print('✨✨ ------------------------------✨✨')
    print('[1] ➕   Registrar un cliente') 
    print('[2] 🗑️   Eliminar un cliente')
    print('[3] 🖋️   Buscar un cliente')
    print('[4] 🔎   Lista de clientes')
    print('[5] 🔎   Lista de clientes preferenciales')
    print('[6] 👣   Salir')

def agregar_estudiante():
    try:
        cedula = int(input('\nIngrese la cédula del estudiante: '))
        if cedula in clientes:
            print('⚠️ El estudiante ya existe. Ingrese otra cédula.')
        else:
            nombre = input('Ingrese el nombre: ').title()
            apellido = input('Ingrese el apellido: ').title()
            clientes [cedula] = {
                'nombre': nombre,
                'apellido': apellido,
                'materias': {}
            }
            print(f'✅ Estudiante {nombre} {apellido} agregado exitosamente!')
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()


def registrar_cliente():
    pass

def eliminar_cliente():
    pass

def listar_clientes():
    print("----- lista de cliente-----")
    for cedula, informacion in clientes.items():
        buscar_cliente(cedula)

def listar_preferenciales():
    pass

def buscar_cliente(cedulaCliente):
    if cedulaCliente in clientes:
        print(f"Cedula cliente: {cedulaCliente}")
        print(f"---Información: ")
        print(f"   NOMBRE: {clientes[cedulaCliente]['NOMBRE']}")
        print(f"   APELLIDO: {clientes[cedulaCliente]['APELLIDO']}")
        print(f"   CORREO: {clientes[cedulaCliente]['CORREO']}")
        print(f"   TELEFONO : {clientes[cedulaCliente]['TELEFONO']}")
        print(f"   DIRECCION: {clientes[cedulaCliente]['DIRECCION']}")
        print(f"   PREFERENCIAL : {   'Preferencial' if (clientes[cedulaCliente]['PREFERENCIAL']) else 'no preferencial'  }  ")

