from Cliente import Cliente
import os

direccion=os.path.join(os.path.dirname(__file__), 'clientes_empresa.txt')

diccionarioVendedores={}

class ReportesMain:

    def __init__(self):
        self.estado=False
        self.listaObjetosCliente=[]

    def agregar_objeto_cliente(self,valor):
        self.listaObjetosCliente.append(valor)

    def importar_datos(self,diccionarioVendedores):
        with open(direccion,"r") as archivo:
            next(archivo)
            for linea in archivo:
                
                temp=linea.split("\t")
                instanciaCliente=Cliente(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12],temp[13],temp[14])
                self.agregar_objeto_cliente(instanciaCliente)
                diccionarioVendedores[temp[11]]=temp[12]
        self.estado=True
        
        print("Datos importados¡¡")

    def clientes_por_vendedor(self,diccionarioVendedores):
        if self.estado==True:
            for key,value in diccionarioVendedores.items():
                print(f"Numero: {key} Nombre: {value}")
            numero=int(input("Ingrese el numero de vendedor: "))
            with open("clientes_por_vendedor.txt","w") as archivo1, open(direccion,"r") as archivo2:
                for linea in archivo2:
                    temp=linea.split("\t")
                    if temp[11]==str(numero):
                        archivo1.write(f"{linea}\n")
                print("Archivo generado¡¡")

        else:
            print("Aun no se genero la lista¡¡")
            return

    def cliente_lista_precio(self):
        if self.estado==True:
            pass
        else:
            print("Aun no se genero la lista¡¡")
            return
        print("1-LISTA PRECIO 1")
        print("2-LISTA PRECIO 2")
        print("3-LISTA PRECIO 3")
        print("4-LISTA PRECIO 4")
        opcion=int(input(""))
        if opcion==1:
            listaprecio="LISTA PRECIO 1"
        elif opcion==2:
            listaprecio="LISTA PRECIO 2"
        elif opcion==3:
            listaprecio="LISTA PRECIO 3"
        elif opcion==4:
            listaprecio="LISTA PRECIO 4"

        with open("clientes_por_vendedor.txt","w") as archivo1, open(direccion,"r") as archivo2:
            for linea in archivo2:
                    temp=linea.split("\t")
                    if temp[13]==str(listaprecio):
                        archivo1.write(f"{linea}\n")
            print("Archivo generado¡¡")



    def cliente_rango_saldo(self):
        if self.estado==True:
            pass
        else:
            print("Aun no se genero la lista¡¡")
            return
        valorminimo=float(input("Ingrese el valor minimo: "))
        valormaximo=float(input("Ingrese el valor maximo: "))
        if valorminimo>=valormaximo:
            print("El valor mínimo no puede ser igual o mayor al valor máximo")
            return
        with open("clientes_por_rango_saldo.txt","w") as archivo1, open(direccion,"r") as archivo2:
            next(archivo2)
            for linea in archivo2:
                temp=linea.split("\t")
                valor =temp[14].replace(".", "").strip()
                valor=float(valor.replace(",","."))
                if valorminimo<=valor<=valormaximo:
                    archivo1.write(f"{linea}\n")
            print("Archivo generado¡¡")

    def main(self):

        menu=False

        while menu==False:

            print("----------MENU----------")
            print("a- Importar datos")
            print("b- Clientes por vendedor")
            print("c- Clientes por lista de precio")
            print("d- Clientes por rango Saldo")
            print("e- Salir")
            print("-------------------------")

            opcion=input().lower()

            if opcion=="a":
                self.importar_datos(diccionarioVendedores)

            elif opcion=="b":
                self.clientes_por_vendedor(diccionarioVendedores)

            elif opcion=="c":
                self.cliente_lista_precio()

            elif opcion=="d":
                self.cliente_rango_saldo()

            elif opcion=="e":
                menu=True

            else:
                print("Error de menu")


instanciaMain=ReportesMain()
instanciaMain.main()