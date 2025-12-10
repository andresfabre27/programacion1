from Producto import Producto
from OrdenCompra import OrdenCompra
from DetalleOrdenCompra import DetalleOrdenCompra
import os
from datetime import date

direccion=os.path.join(os.path.dirname(__file__), 'productos_compra.txt')

class GenerarOrdenComprasMain:
    
    def __init__(self):
        self.listaOrdenCompras=[]

    def agregar_listaOrdenCompras(self,value):
        self.listaOrdenCompras.append(value)

    def ver_orden_compra_cargadas(self):
        if len(self.listaOrdenCompras)==0:
            print("No hay ordenes de compra cargadas")
            return -1
        for objeto in self.listaOrdenCompras:
            print(f"Numero de Orden: {objeto.numero} Fecha: {objeto.fecha} Total: {objeto.total}")



    def cargar_orden_compra(self,ProductosDataBase):
        
        while True:

            fecha=date.today()
            numero=len(self.listaOrdenCompras)+1
            instanciaOrdenCompra=OrdenCompra(fecha,numero)
            self.agregar_listaOrdenCompras(instanciaOrdenCompra)

            while True:

                while True:
                    codigo=str(input("Ingrese el codigo del producto: "))
                    
                    if codigo in ProductosDataBase:
                        break
                    else:
                        print("Producto no encontrado, intente nuevamente")

                cantidad=int(input("Ingrese la cantidad: "))
                objeto=ProductosDataBase[codigo]
                subtotal=int(objeto.precioCompra)*cantidad
                instanciaDetalleOrdenCompra=DetalleOrdenCompra(cantidad,objeto,subtotal)
                instanciaOrdenCompra.agregar_listaDetalles(instanciaDetalleOrdenCompra)
                instanciaOrdenCompra.total+=subtotal

                opcion1=input("¿Desea agregar otro producto? Si/No: ")
                if opcion1=="No":
                    break
                elif opcion1=="Si":
                    pass
            print("Orden de compra generada¡¡")
            opcion2=input("¿Desea agregar otra Orden de Compra? Si/No: ")
            if opcion2=="No":
                break
            elif opcion2=="Si":
                pass    




    def generar_orden_por_numero(self):
        if len(self.listaOrdenCompras)==0:
            print("No hay ordenes de compra cargadas")
            return -1
        numero=int(input("Ingrese el numero de orden: "))
        encontrado=False
        for objeto in self.listaOrdenCompras:
            if objeto.numero==numero:
                objeto1=objeto
                encontrado=True
                break
        if encontrado==True:
            print(f"Orden de compra numero: {objeto1.numero}")
            print(f"Fecha: {objeto1.fecha}")
            print("----------Productos comprados----------") 
            print("Código | Denominación | Rubro| Marca | Cantidad | SubTotal")
            for obj in objeto1.listaDetalles:
                objeto2=obj.producto
                print(f"{objeto2.codigo} | {objeto2.denominacion} | {objeto2.rubro} | {objeto2.marca} | {obj.cantidad} | {obj.subtotal}")
            print(f"TOTAL: {objeto1.total}")

            opcion=input("¿Desea imprimir la orden? Si/No: ")
            if opcion=="Si":
                nombre=f"ordenCompra_nro_{objeto1.numero}.txt"
                with open(nombre,"w") as archivo:
                    archivo.write(f"Orden de compra numero: {objeto1.numero}\n")
                    archivo.write(f"Fecha: {objeto1.fecha}\n")
                    archivo.write("----------Productos comprados----------\n") 
                    archivo.write("Código | Denominación | Rubro| Marca | Cantidad | SubTotal\n")
                    for obj in objeto1.listaDetalles:
                        objeto2=obj.producto
                        archivo.write(f"{objeto2.codigo} | {objeto2.denominacion} | {objeto2.rubro} | {objeto2.marca} | {obj.cantidad} | {obj.subtotal}\n")
                    archivo.write(f"TOTAL: {objeto1.total}")    
                print("Archivo generado¡¡")


        else:
            print("Orden de compra no encontrada")
            return -1


    def main(self):
        
        ProductosDataBase={}

        with open(direccion,"r") as archivo:
            for linea in archivo:
                temp=linea.split(";")
                codigo,denominacion,rubro,marca,preciocompra=temp
                instanciaProducto=Producto(codigo,denominacion,rubro,marca,preciocompra)
                ProductosDataBase[temp[0]]=instanciaProducto
            

        menu=False

        while menu==False:
            
            print("-------------MENU----------------")
            print("A- Ver Orden de Compras Cargadas")
            print("B- Cargar 1 o más Órdenes de Compra")
            print("C- Generar Archivo Orden de Compra por numero")
            print("D- Salir")
            print("----------------------------------")
            opcion=input("")

            if opcion=="A":
                self.ver_orden_compra_cargadas()

            elif opcion=="B":
                self.cargar_orden_compra(ProductosDataBase)

            elif opcion=="C":
                self.generar_orden_por_numero()

            elif opcion=="D":
                menu=True

            else:
                print("Error de menu")


instanciaGenerarOrdenComprasMain=GenerarOrdenComprasMain()
instanciaGenerarOrdenComprasMain.main()