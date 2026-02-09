from Articulo import Articulo
from RemitoVenta import RemitoVenta
from RemitoVentaDetalle import RemitoVentaDetalle
from RepartoDiario import RepartoDiario



class CrearRepartoDiario:
    def __init__(self):

        self.articulosDisponibles=[Articulo(10, "Filtro de Aceite", 10000),
                                   Articulo(20, "Filtro de Aire", 8000),
                                   Articulo(30, "Filtro de Combustible", 7500),
                                   Articulo(40, "Aceite de Motor sw/10", 25000),
                                   Articulo(50, "Correa de Distribución", 20000)
                                   ]
        
        self.clientesReparto={20284569875 : "Juan Alonso",
                              20157896542 : "Emiliano Salas",
                              50258963654 : "Pacallcar Autos",
                              27654987456 : "Julieta Videla",
                              50335588945 : "Todo Auto SRL"
                              }
        
    def main(self):
        
        fecha=input("Ingrese la fecha de reparto: ")
        instaciaRepartoDiario=RepartoDiario(fecha)

        while True:
           
            cuit=int(input("Ingrese el numero de cuit del cliente: "))
            if cuit not in self.clientesReparto.keys():
                print("El cuit no se encuentra, procedemos a agregarlo")
                nombre=input("Ingrese el Nombre: ")
                self.clientesReparto[cuit]=nombre
                print("Cliente cargado¡¡")
            else:
                print("Cliente encontrado¡¡")
                nombre=self.clientesReparto[cuit]
    
            numero=input("Ingrese el numero de remito: ")
            instanciaRemitoVenta=RemitoVenta(nombre,numero)
            instaciaRepartoDiario.agregar_remitosVenta(instanciaRemitoVenta)

            while True:
               
                while True:
                    codigoArticulo=int(input("Ingrese el codigo del articulo: "))
                    encontrado=False
                    for obj in self.articulosDisponibles:
                        if obj.codigo==codigoArticulo:
                           posicion=obj
                           encontrado=True
                           break
                    
                    if encontrado==False:
                        print("Articulo no encontrado¡¡")
                    else:
                        print("Articulo encontrado¡¡")
                        break
                
                

                cantidad=int(input("Ingrese la cantidad: "))
                while cantidad<=0:
                    print("La cantidad debe ser mayor a cero¡¡")
                    cantidad=int(input("Ingrese la cantidad: "))

                instanciaRemitoVentaDetalle=RemitoVentaDetalle(cantidad,posicion)
                instanciaRemitoVenta.agregarDetallesRemito(instanciaRemitoVentaDetalle)
                #instanciaRemitoVentaDetalle.subtotal=cantidad*posicion.precio
                instanciaRemitoVenta.totalVenta+=instanciaRemitoVentaDetalle.subtotal

                opcion1=input("¿Desea agregar otro articulo? S/N: ").upper()
                if opcion1=="N":
                    break
                elif opcion1=="S":
                    pass
            
            instaciaRepartoDiario.totalReparto+=instanciaRemitoVenta.totalVenta
            opcion2=input("¿Desea agregar otro remito? S/N: ").upper()
            if opcion2=="N":
                break
            elif opcion2=="S":
                pass

        print("Reparto diario")
        print(f"Fecha: {instaciaRepartoDiario.fecha} ")
        print("------Remitos del reparto------")
        for objeto1 in instaciaRepartoDiario.remitosVenta:
            print(f"Nombre Cliente: {objeto1.nombreCliente}")
            print(f"Numero Remito: {objeto1.numeroRemito}")
            for objeto2 in objeto1.detallesRemito:
                objeto3=objeto2.articulo
                print("Cantidad Items| Denominación Articulo | Precio Unitario | Subtotal")
                print(f"{objeto2.cantidad} | {objeto3.denominacion} | {objeto3.precio}| {objeto2.subtotal}")
            print(f"Total Remito Venta: {objeto1.totalVenta}")
            print("----------------------------")
        print(f"Monto Total Reparto: {instaciaRepartoDiario.totalReparto}")

instanciaCrearRepartoDiario=CrearRepartoDiario()
instanciaCrearRepartoDiario.main()
               

