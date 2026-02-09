from DetalleOrdenCompra import DetalleOrdenCompra
from OrdenCompra import OrdenCompra
from Producto import Producto
from datetime import date
import os

direccion=os.path.join(os.path.dirname(__file__), 'productos_compra.txt')
os.path.join(os.path.dirname(__file__), 'ordenCompra_nro_.txt')




class GenerarOrdenComprasMain:
 
    def __init__(self):
        self.ProductosDataBase={}
        self.listaOrdenCompras=[]


    def agregar_listaOrdenCompras(self,valor):
        self.listaOrdenCompras.append(valor)
        
    def generador(self):
        with open(direccion,"r") as archivo:
            next(archivo)
            for linea in archivo:
                temp=linea.split(";")
                instanciaProducto=Producto(temp[0].strip(),temp[1].strip(),temp[2].strip(),temp[3].strip(),int(temp[4].strip()))
                self.ProductosDataBase[int(temp[0])]=instanciaProducto
        

    def ver_orden_compra(self):
        if len(self.listaOrdenCompras)==0:
            print("No hay ordenes de compras cargadas!!")
            return
        print("---------Ordenes de compra cargadas------------")
        for obj in self.listaOrdenCompras:
            print(f"Fecha: {obj.fecha} Numero: {obj.numero} Total: {obj.total}")

    def cargar_orden_compra(self):
        
        while True:
            fecha=date.today()
            instanciaOrdenCompra=OrdenCompra(fecha)
            instanciaOrdenCompra.numero=len(self.listaOrdenCompras)+1
            self.agregar_listaOrdenCompras(instanciaOrdenCompra)
            

            while True:
                
                encontrado=False
                while True:
                    codigoProducto=int(input("Ingrese el codigo del producto: "))
                    for key in self.ProductosDataBase.keys():
                        if codigoProducto==key:
                            encontrado=True
                            objeto=self.ProductosDataBase[codigoProducto]
                            break
                    if encontrado==True:
                        print("Articulo encontrado!!")
                        break
                    else:
                        print("Articulo no encontrado!!")

                cantidad=int(input("Ingrese la cantidad a llevar: "))  
                #subtotal=cantidad*int(objeto.precioCompra)
                instanciaDetalleOrdenCompra=DetalleOrdenCompra(cantidad,objeto)
                instanciaOrdenCompra.agregar_listaDetalles(instanciaDetalleOrdenCompra)
                
                instanciaOrdenCompra.total+=instanciaDetalleOrdenCompra.subtotal
                
                

                opcion1=input("¿Desea agregar otro producto? S/N: ").upper()

                if opcion1=="N":
                    break
                elif opcion1=="S":
                    pass
            
            
            print("Orden de compra cargada!!")
            opcion2=input("¿Desea agregar otra Orden de compra? S/N: ").upper()

            if opcion2=="N":
                break
            elif opcion2=="S":
                pass


    def orden_compra_por_numero(self):
        
        encontrado=False
        numero=int(input("Ingrese el numero de la orden de compra: "))
        for obj in self.listaOrdenCompras:
            if numero==obj.numero:
                encontrado=True
                objeto=obj
        if encontrado==False:
            print(f"Orden numero {numero} no encontrada!!")
            return
        
        print(f"Orden de compra numero: {objeto.numero}")
        print(f"fecha: {objeto.fecha}")
        print("---------Productos Comprados------------")
        print("Código | Denominación | Rubro | Marca | Cantidad | SubTotal")

        for objeto2 in objeto.listaDetalles:
            objeto3=objeto2.producto
            print(f"{objeto3.codigo} | {objeto3.denominacion} | {objeto3.rubro} | {objeto3.marca} | {objeto2.cantidad} | {objeto2.subtotal}")
        print(f"Total: {objeto.total}")

        opcion=input("¿Desea generar el archivo oden de compra? S/N: ").upper()
        if opcion=="N":
            return
        elif opcion=="S":
            palabra="ordenCompra_nro_"+str(objeto.numero)+".txt"
            with open(os.path.join(os.path.dirname(__file__), palabra),"w") as archivo:

                archivo.write(f"Orden de compra numero: {objeto.numero}\n")
                archivo.write(f"fecha: {objeto.fecha}\n")
                archivo.write("---------Productos Comprados------------\n")
                archivo.write("Código | Denominación | Rubro | Marca | Cantidad | SubTotal\n")

                for objeto2 in objeto.listaDetalles:
                    objeto3=objeto2.producto
                    archivo.write(f"{objeto3.codigo} | {objeto3.denominacion} | {objeto3.rubro} | {objeto3.marca} | {objeto2.cantidad} | {objeto2.subtotal}\n")
                archivo.write(f"Total: {objeto.total}\n")
                print("Archivo generado!!")




            


    def main(self):
        
        self.generador()

        menu=False
        while menu==False:

            print("--------MENU--------")
            print("a- Ver Orden de Compras Cargadas")
            print("b- Cargar 1 o más Órdenes de Compra")
            print("c- Generar Archivo Orden de Compra por numero")
            print("d- Salir")
            print("---------------------")
            opcion=input().lower()

            if opcion=="a":
                self.ver_orden_compra()

            elif opcion=="b":
                self.cargar_orden_compra()

            elif opcion=="c":
                self.orden_compra_por_numero()
            
            elif opcion=="d":
                menu=True

            else:
                print("Error de menu!!")


intanciaMain=GenerarOrdenComprasMain()
intanciaMain.main()
