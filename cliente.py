class Cliente:

    def __init__(self,id: int, nombre: str, telefono: int, correo:str, direccion:str, monto:int = 0):
        self.id = id  
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.monto = monto
        self.reservas = []
    

    #implementar
    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.telefono}, {self.correo}, {self.direccion}, {self.monto}"
        



    @classmethod
    def cargar_cliente_input(cls): 
        cliente = {
        'id': int(input("Ingrese id: ")),
        'nombre': input("Ingrese nombre: "),
        'telefono': int(input("Ingrese teléfono: ")),
        'correo': input("Ingrese correo: "),
        'direccion': input("Ingrese dirección: ")
        }
        return cls(cliente)

    def arrendar(self):
        print(f'{self.nombre} ha arrendado una bicicleta')
    
    def reservar(self):
        self.reservas.append("bicicleta")
        print(f"{self.nombre} ha reservado una bicicleta.")

    def mostrar_reservas(self):
        if self.reservas:
            print(f"Reservas de {self.nombre}:")
            for i, r in enumerate(self.reservas, 1):
                print(f" {i}. {r}")
        else:
            print(f"{self.nombre} no tiene reservas.")