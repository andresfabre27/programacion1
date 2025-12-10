from Producto import Producto
from OrdenCompra import OrdenCompra
from DetalleOrdenCompra import DetalleOrdenCompra
import os
from datetime import date

direccion = os.path.join(os.path.dirname(__file__), 'productos_compra.txt')

class GenerarOrdenComprasMain:

    def __init__(self):
        self.listaOrdenCompras = []

    def ver_orden_compra_cargadas(self):
        if len(self.listaOrdenCompras) == 0:
            print("No hay órdenes cargadas.")
            return
        
        print("ÓRDENES CARGADAS:")
        for oc in self.listaOrdenCompras:
            print(f"NRO: {oc.numero}  FECHA: {oc.fecha}  TOTAL: {oc.total}")

    def cargar_orden_compra(self, ProductosDataBase):
        numero = len(self.listaOrdenCompras) + 1
        fecha = date.today()
        instanciaOrden = OrdenCompra(fecha, numero)

        print(f"\nCargando Orden de Compra N° {numero}\n")

        while True:
            # validar código
            while True:
                try:
                    codigo = int(input("Ingrese el código del producto: "))
                except:
                    print("Debe ingresar un número.")
                    continue

                if codigo in ProductosDataBase:
                    break
                else:
                    print("El código no existe, intente otra vez.")

            # validar cantidad
            while True:
                try:
                    cantidad = int(input("Ingrese cantidad: "))
                    if cantidad > 0:
                        break
                    else:
                        print("La cantidad debe ser mayor a 0.")
                except:
                    print("Debe ingresar un número entero.")

            producto = ProductosDataBase[codigo]
            subtotal = int(producto.precioCompra) * cantidad

            detalle = DetalleOrdenCompra(cantidad, producto, subtotal)
            instanciaOrden.agregar_listaDetalles(detalle)

            seguir = input("¿Desea cargar otro detalle? S/N: ").upper()
            if seguir != "S":
                break

        if len(instanciaOrden.listaDetalles) == 0:
            print("Debe ingresar al menos un detalle. Orden no guardada.")
            return

        self.listaOrdenCompras.append(instanciaOrden)
        print("\nOrden de compra cargada con éxito.\n")

    def generar_orden_por_numero(self):
        if len(self.listaOrdenCompras) == 0:
            print("No hay órdenes cargadas.")
            return

        try:
            nro = int(input("Ingrese el número de Orden: "))
        except:
            print("Debe ingresar un número.")
            return

        ordenEncontrada = None
        for oc in self.listaOrdenCompras:
            if oc.numero == nro:
                ordenEncontrada = oc
                break

        if ordenEncontrada is None:
            print(f"La Orden de Compra con número {nro} no existe.")
            return

        # mostrar la orden por pantalla
        print(f"\nOrden de Compra N° {ordenEncontrada.numero}")
        print(f"Fecha: {ordenEncontrada.fecha}")
        print("------------ Productos Comprados ------------------------")
        print("Código | Denominación | Rubro | Marca | Cantidad | Subtotal")

        for det in ordenEncontrada.listaDetalles:
            p = det.producto
            print(f"{p.codigo} | {p.denominacion} | {p.rubro} | {p.marca} | {det.cantidad} | {det.subtotal}")

        print(f"TOTAL: {ordenEncontrada.total}\n")

        # generar archivo?
        opcion = input("¿Desea generar archivo TXT? (S/N): ").upper()
        if opcion == "S":
            nombre = f"ordenCompra_nro_{ordenEncontrada.numero}.txt"
            with open(nombre, "w", encoding="utf-8") as f:
                f.write(f"Orden de Compra N° {ordenEncontrada.numero}\n")
                f.write(f"Fecha: {ordenEncontrada.fecha}\n")
                f.write("------------ Productos Comprados ------------------------\n")
                f.write("Código | Denominación | Rubro | Marca | Cantidad | Subtotal\n")

                for det in ordenEncontrada.listaDetalles:
                    p = det.producto
                    f.write(f"{p.codigo} | {p.denominacion} | {p.rubro} | {p.marca} | {det.cantidad} | {det.subtotal}\n")

                f.write(f"\nTOTAL: {ordenEncontrada.total}")

            print("Archivo generado correctamente.\n")

    def main(self):
        # Cargar la base de datos de productos
        ProductosDataBase = {}

        with open(direccion, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                temp = linea.strip().split(";")
                codigo, denominacion, rubro, marca, preciocompra = temp
                instanciaProducto = Producto(int(codigo), denominacion, rubro, marca, int(preciocompra))
                ProductosDataBase[int(codigo)] = instanciaProducto

        # menú
        while True:
            print("-------------MENU----------------")
            print("A- Ver Órdenes Cargadas")
            print("B- Cargar Órdenes de Compra")
            print("C- Generar Archivo por Número de Orden")
            print("D- Salir")
            print("----------------------------------")

            opcion = input("Ingrese opción: ").upper()

            if opcion == "A":
                self.ver_orden_compra_cargadas()
            elif opcion == "B":
                self.cargar_orden_compra(ProductosDataBase)
            elif opcion == "C":
                self.generar_orden_por_numero()
            elif opcion == "D":
                print("Fin del programa.")
                break
            else:
                print("Opción incorrecta.")


instancia = GenerarOrdenComprasMain()
instancia.main()