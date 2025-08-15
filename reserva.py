from datetime import datetime
class ReservaInvalidaError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)

class Reserva:

    def __init__ (self, cliente, bicicleta, inicio, fin):
        try:
            if not isinstance(inicio, datetime) or not isinstance(fin, datetime):
                raise ReservaInvalidaError("Las fechas deben ser objetos datetime")
            if fin <= inicio:
                raise ReservaInvalidaError ("La fecha de fin de la reserva debe ser posterior a la fecha de inicio")
            if bicicleta.disponible == False:
            #if not getattr(bicicleta,"disponible", None):
                raise ReservaInvalidaError(f"La bicicleta no está disponible.")
            self.cliente = cliente
            self.bicicleta = bicicleta
            self.inicio = inicio
            self.fin = fin
            self.costo = self.calcular_costo()
            bicicleta.arrendar()

            print(f"✅¡Reserva creada para {cliente.nombre} en la bicicleta {bicicleta.id} desde las {inicio.strftime("%I:%M %p")} hasta las {fin.strftime("%I:%M %p")} horas!")
            #print(f"✅ Agendado para cliente{cliente_seleccionado.nombre} en la bicicleta {bicicleta_seleccionada.id} por {timedelta(hours = horas_seleccion)} horas.")

            print(f"EL valor total a pagar es de : $ {self.costo}")

        except(ReservaInvalidaError)as r:
            print(f"Error al crear la reserva {r}")
            raise

    def __str__(self):
        return f" Cliente: {self.cliente.nombre} - Bicicleta: {self.bicicleta.id} - Inicio: {self.inicio} - Fin: {self.fin} - Costo: ${self.costo}"
        
    def calcular_costo(self):
        duracion_horas = round((self.fin - self.inicio).total_seconds() / 3600)
        return round(duracion_horas * self.bicicleta.precio_hora)
    

    
    def finalizar(self):
        self.bicicleta.disponible = True #bici
        print(f"Reserva Finalizada. La bicicleta {self.bicicleta.id} quedó disponible nuevamente") 

