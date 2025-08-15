import bicicleta as bici
import cliente as cli
import reserva as res
from datetime import datetime, timedelta

class Sistema:

    def __init__(self):
        self.bicicletas = {}
        self.reservas = {}
        self.reservas_activas = {}
        self.clientes = {}
        self.opciones = ["Agregar cliente","Agregar bicicleta", "Crear Reserva", "Finalizar Reserva"]
        self.numero_reservas = 0

    def agregar_cliente(self, cliente= None):
        
        if cliente == None:
            nuevo_cliente = cli.Cliente.cargar_cliente_input()
        else:
            nuevo_cliente = cliente   

        if not isinstance(nuevo_cliente, cli.Cliente):
            raise res.ReservaInvalidaError(mensaje="NO ES OBJETO CLIENTE")

        try:
            if nuevo_cliente.id in self.clientes:
                raise res.ReservaInvalidaError(mensaje="⚠️ DUPLICADO")
            
            self.clientes[nuevo_cliente.id] = nuevo_cliente
            print("✅ Nuevo cliente ha sido agregado")     
        except res.ReservaInvalidaError as e:
            print(e.mensaje)
        except Exception as e:
            print(f"🛑 {e}") 

        
    def agregar_bicicleta(self, bicicleta= None):
        if bicicleta == None:
            print("Ingrese los datos de la bicicleta:")
            nueva_bicicleta = bici.Bicicleta.cargar_bicicleta_input()
        else:
            nueva_bicicleta = bicicleta

        try:
            if nueva_bicicleta.id in self.bicicletas:
                raise res.ReservaInvalidaError(mensaje="⚠️ DUPLICADO")
            
            self.bicicletas[nueva_bicicleta.id] = nueva_bicicleta        
            print("✅ Bicicleta ingresada")
        except res.ReservaInvalidaError as e:
            print(e.mensaje)
        except Exception as e:
            print(f"🛑 {e}")     


    def crear_reserva(self, cliente_id_seleccion =None, bicicleta_id_seleccion = None, horas_seleccion = None):

        if cliente_id_seleccion == None:
            sistema.revisar_clientes()
            cliente_id_seleccion = int(input("Ingrese el id del cliente: "))

        try:
            if cliente_id_seleccion < 0:
                raise ValueError
            if cliente_id_seleccion not in sistema.clientes.keys():
                raise IndexError
        except ValueError:
            print("⚠️ Debes ingresar un número valido.")
            return
        except IndexError:
            print("⚠️ Debes ingresar un cliente dentro de nuestro catalogo.")
            return
        except Exception as e:
            print(f"🛑 Ha ocurrido un error inesperado: {e}")
            return

        cliente_seleccionado = sistema.clientes[cliente_id_seleccion]

        if bicicleta_id_seleccion == None:
            sistema.revisar_bicicletas()
            bicicleta_id_seleccion = (input("Ingrese el nombre de la bicicleta: "))
        
        try:
            if bicicleta_id_seleccion == "":
                raise ValueError
            if bicicleta_id_seleccion not in sistema.bicicletas.keys():
                raise IndexError
            if bicicleta_id_seleccion in sistema.bicicletas.keys() and sistema.bicicletas[bicicleta_id_seleccion].disponible == False:
                raise res.ReservaInvalidaError(mensaje="⚠️ La bicicleta seleccionada no esta disponible.")
        except ValueError:
            print("⚠️ Debes ingresar un texto valido.")
            return
        except IndexError:
            print("⚠️ Debes ingresar una bicicleta dentro de nuestro catalogo.")
            return    
        except res.ReservaInvalidaError as e:
            print(e.mensaje)
            return
        
        bicicleta_seleccionada = sistema.bicicletas[bicicleta_id_seleccion]

        if horas_seleccion == None:
            horas_seleccion = int(input("Ingrese cuantas horas va a usar la bicicleta: "))
        try: 
            if horas_seleccion < 0:
                raise ValueError
        except ValueError: 
            print("⚠️ Debes ingresar un número valido.")
            return
        except Exception as e:
            print(f"🛑 Ha ocurrido un error inesperado: {e}")
            return
        
        nueva_reserva = res.Reserva(cliente_seleccionado,bicicleta_seleccionada,datetime.now(),datetime.now() + timedelta(hours = horas_seleccion))
        self.reservas_activas[self.numero_reservas] = nueva_reserva
        self.numero_reservas += 1


    def finalizar_reserva(self, reserva_id = None):
        sistema.historial_de_reservas()
        
        if reserva_id == None:
            reserva_id = int(input("Ingrese el id de la reserva que quieres dar por completa: "))
        try:
            if reserva_id in self.reservas_activas:
                reserva_seleccionada = self.reservas_activas[reserva_id]
            else:
                raise KeyError
        except KeyError:
            print("⚠️ Debes ingresar una reserva dentro de nuestro catalogo.")
            return
        except Exception as e:
            print(f"🛑 Ha ocurrido un error inesperado: {e}")
            return
        
        reserva_seleccionada.finalizar()
        self.reservas_activas.pop(reserva_id)

    def historial_de_reservas(self):
        for clave, reserva in self.reservas_activas.items():
            print(f"Id reserva: {clave}:{reserva}")

    def revisar_bicicletas(self):
        print("bicicletas: ")    
        for bicicleta in self.bicicletas.values():
            print(bicicleta)

    def revisar_clientes(self):
        print("clientes id: ")
        for cliente in self.clientes.values():
            print(cliente)

    def ejecutar(self):
        while(True):
            print("\n🚲🚲🚲🚲Bienvenidos a BIKECITY🚲🚲🚲🚲 \n")
            for i, o in enumerate(self.opciones):
                print(i,o)
            opcion = input("Selecciona una opcion: ")
            if opcion == "0":
                self.agregar_cliente()
            elif opcion == "1":
                self.agregar_bicicleta()
            elif opcion == "2":
                self.crear_reserva()
            elif opcion == "3":
                self.finalizar_reserva()
                #self.historial_de_reservas()
            #elif opcion == "4":
                #self.revisar_bicicletas()
            #elif opcion == "5":
                #self.revisar_clientes()    
            else:
                print("Opcion no valida")


sistema = Sistema()
#cosas pa testear
sistema.agregar_cliente(cli.Cliente(id= 1,nombre= "Piero",telefono= 9564554545,correo= "correo@mail.com",direccion= "casita 123"))
sistema.agregar_cliente(cli.Cliente(id= 1,nombre= "sdasdsd",telefono= 9564554545,correo= "correo@mail.com",direccion= "casita 123"))
sistema.agregar_bicicleta(bici.Bicicleta(id="bici_1",precio_hora= 800, estado= "buena"))
sistema.agregar_bicicleta(bici.Bicicleta(id="bici_2",precio_hora= 1800, estado= "buena"))
sistema.crear_reserva(1,"bici_1",5)
sistema.ejecutar()




