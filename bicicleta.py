class Bicicleta:
    def __init__(self, id: str, precio_hora: int, estado: str = "buena"):
        self.id = id
        self.disponible = True
        self.precio_hora = precio_hora
        self.estado = "buena"

    def __str__(self):
        if self.disponible:
            disponibilidad = "Disponible" 
        else:
            disponibilidad = "No disponible"

        return (
            f"Bicicleta ID: {self.id} | "
            f"Estado: {self.estado} | "
            f"Precio/hora: $ {self.precio_hora} | "
            f"{disponibilidad}")
    @classmethod
    def cargar_bicicleta_input(cls): #aqui agregar los try except para la validacion
        id = input("Ingrese nombre: ")
        precio_hora = int(input("Ingrese precio-hora: "))
        return cls(id, precio_hora)

    def arrendar(self):
        if not self.disponible:
            raise Exception("La bicicleta ya está arrendada.")
        if self.estado != "buena":
            raise Exception(f"No se puede arrendar una bicicleta en estado '{self.estado}'.")
        self.disponible = False
        print(f"Bicicleta {self.id} arrendada correctamente.")

    def liberar(self):
        self.disponible = True
        print(f"Bicicleta {self.id} ahora está disponible.")

    def reparar(self):
        if self.estado != "buena":
            self.estado = "buena"
            print(f"Bicicleta {self.id} ha sido reparada y está en buen estado.")
        else:
            print(f"Bicicleta {self.id} ya está en buen estado.")
