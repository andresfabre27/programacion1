from Articulo import Articulo
from RemitoVenta import RemitoVenta
from RemitoVentaDetalle import RemitoVentaDetalle
from RepartoDiario import RepartoDiario



class CrearRepartoDiario:
    
    def buscar_codigoarticulo(self,articulosDisponibles,codigoarticulo):

        for i in range(len(articulosDisponibles)):
                    if articulosDisponibles[i][0]==codigoarticulo:
                         return i
        return -1

    def main(self):
        
        articulosDisponibles=[[10, "Filtro de Aceite", 10000],
                              [20, "Filtro de Aire", 8000],
                              [30, "Filtro de Combustible", 7500],
                              [40, "Aceite de Motor sw/10", 25000],
                              [50, "Correa de Distribución", 20000]
                              ]
        
        clientesReparto={20284569875 : "Juan Alonso",
                         20157896542 : "Emiliano Salas",
                         50258963654 : "Pacallcar Autos",
                         27654987456 : "Julieta Videla",
                         50335588945 : "Todo Auto SRL"
                         }
        
        fechaReparto=input("Indique la fecha del reparto: ")
        instanciaRepartoDiario=RepartoDiario(fechaReparto)

        while True:
            
            print("Ingrese los datos del remito")
            nombreCliente=input("Ingrese el nombre del cliente: ")
            legajo=int(input("Ingrese el legajo: "))
            if legajo not in clientesReparto.keys():
                clientesReparto[legajo]=nombreCliente
                print("Legajo Creado")
            numeroRemito=int(input("Ingrese el numero del remito: "))
            instanciaRemitoVenta=RemitoVenta(nombreCliente,numeroRemito)
            instanciaRepartoDiario.agregar_remitosVenta(instanciaRemitoVenta)

            print("Ingrese los detalles de la venta: ")

            while True:
                
                encontrado=False
                while encontrado==False:
                    codigoarticulo=int(input("Ingrese el codigo del articulo: "))
                    
                    for linea in articulosDisponibles:
                        for elemento in linea:
                            if codigoarticulo==elemento:
                                encontrado=True
                    if encontrado==False:
                        print("El codigo es incorrecto")  

                indice=self.buscar_codigoarticulo(articulosDisponibles,codigoarticulo)
                

                codigo=articulosDisponibles[indice][0]
                denominacion=articulosDisponibles[indice][1]
                precio=articulosDisponibles[indice][2]
                instanciaArticulo=Articulo(codigo,denominacion,precio)

                cantidad=int(input("Ingrese la cantidad: ")) 
                subtotal=precio*cantidad

                instanciaRemitoVentaDetalle=RemitoVentaDetalle(cantidad,instanciaArticulo,subtotal)
                instanciaRemitoVenta.agregar_detallesRemito(instanciaRemitoVentaDetalle)
                instanciaRemitoVenta.totalVenta+=subtotal

                salir1=input("¿Desea agregar otro detalle? Si/No: ")
                if salir1=="No":
                     
                     break
                
            instanciaRepartoDiario.totalReparto+=instanciaRemitoVenta.totalVenta

            salir2=input("¿Desea agregar otro remito? Si/No: ") 
            if salir2=="No":
                 break             
                            
        print("Reparto Diario")
        print(f"Fecha: {fechaReparto}")
        print("--------Remitos del reparto-------")

        for objeto in instanciaRepartoDiario.remitosVenta:
             print(f"Nombre del cliente: {objeto.nombreCliente}")
             print(f"Numero remito: {objeto.numeroRemito}")
             for elemento in objeto.detallesRemito:
                  print("Cantidad Items  Denominación Articulo  Precio Unitario  Subtotal")
                  print(f"        {elemento.cantidad}  {elemento.denominacion}   {elemento.precio}          {elemento.subtotal}")
             print(f"Total remito venta: {objeto.totalVenta}")

instanciaMain=CrearRepartoDiario()
instanciaMain.main()                   

                
#{elemento.articulo.denominacion}
#{elemento.articulo.precio}