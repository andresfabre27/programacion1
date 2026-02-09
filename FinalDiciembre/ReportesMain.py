#clase main
from Cliente import Cliente
import os

direccion=os.path.join(os.path.dirname(__file__), 'clientes_empresa.txt')
direccion2=os.path.join(os.path.dirname(__file__), 'clientes_por_vendedor.txt')
direccion3=os.path.join(os.path.dirname(__file__), 'clientes_por_lista_precio.txt')
direccion4=os.path.join(os.path.dirname(__file__), 'clientes_por_rango_saldo.txt')

class ReportesMain:

    def __init__(self):
        self.datosimportados=False
        self.listaCliente=[]
        self.diccionarioVendedores={}

    def agregar_listaCliente(self,valor):
        self.listaCliente.append(valor)

    def importar_datos(self):

        with open(direccion,"r") as archivo:
            next(archivo)
            for linea in archivo:
                temp=linea.split("\t")
                instanciaCliente=Cliente(temp[0].strip(),temp[1].strip(),temp[2].strip(),temp[3].strip(),temp[4].strip(),temp[5].strip(),temp[6].strip(),temp[7].strip(),temp[8].strip(),temp[9].strip(),temp[10].strip(),temp[11].strip(),temp[12].strip(),temp[13].strip(),temp[14].strip(),)
                self.agregar_listaCliente(instanciaCliente)
                self.diccionarioVendedores[temp[11]]=temp[12]
            print("Datos Importados¡¡")
            self.datosimportados=True

    def clientes_por_vendedor(self):

        if self.datosimportados==False:
            print("Datos no importados¡¡")
            return
        else:
            print(self.diccionarioVendedores)
            numero=input("Ingrese el codigo del vendedor: ")

            with open(direccion2,"w") as archivo:
                for objeto in self.listaCliente:
                    if numero==objeto.codigoVendedor:
                        archivo.write(f"{objeto.fechaAlta} {objeto.codigo} {objeto.nroDocumento} {objeto.razonSocial} {objeto.telefono} {objeto.email} {objeto.condicionIva} {objeto.domicilio} {objeto.departamento} {objeto.provincia} {objeto.zona} {objeto.codigoVendedor} {objeto.vendedor} {objeto.listaPrecio} {objeto.saldo}\n")
            print("Arhivo generado¡¡")

    def cliente_lista_precio(self):
        if self.datosimportados==False:
            print("Datos no importados¡¡")
            return
        else:
            print("1- LISTA PRECIO 1")
            print("2- LISTA PRECIO 2")
            print("3- LISTA PRECIO 3")
            print("4- LISTA PRECIO 4")
            opcion=int(input())
            if opcion==1:
                buscar="LISTA PRECIO 1"
            elif opcion==2:
                buscar="LISTA PRECIO 2"
            elif opcion==3:
                buscar="LISTA PRECIO 3"
            elif opcion==4:
                buscar="LISTA PRECIO 4"

            with open(direccion3,"w") as archivo:
                for objeto in self.listaCliente:
                    if buscar==objeto.listaPrecio:
                        archivo.write(f"{objeto.fechaAlta} {objeto.codigo} {objeto.nroDocumento} {objeto.razonSocial} {objeto.telefono} {objeto.email} {objeto.condicionIva} {objeto.domicilio} {objeto.departamento} {objeto.provincia} {objeto.zona} {objeto.codigoVendedor} {objeto.vendedor} {objeto.listaPrecio} {objeto.saldo}\n")
        print("Arhivo generado¡¡")

    def cliente_rango_saldo(self):
        if self.datosimportados==False:
            print("Datos no importados¡¡")
            return
        else:
             
            while True:
                valorminimo=float(input("Ingrese el valor minimo a buscar: "))
                valormaximo=float(input("Ingrese el valor maximo a buscar: "))
                if valorminimo<valormaximo:
                    break
                elif valorminimo>=valormaximo:
                    print("El valor minimo no puede ser mayor o igual que el valor maximo")
                    return
            with open(direccion4,"w") as archivo:   
                for objeto in self.listaCliente:
                    buscar=(objeto.saldo).strip()
                    buscar=buscar.replace(".","")
                    buscar=buscar.replace(",",".")
                    buscar=float(buscar)
                    if valorminimo<=buscar<=valormaximo:
                        archivo.write(f"{objeto.fechaAlta} {objeto.codigo} {objeto.nroDocumento} {objeto.razonSocial} {objeto.telefono} {objeto.email} {objeto.condicionIva} {objeto.domicilio} {objeto.departamento} {objeto.provincia} {objeto.zona} {objeto.codigoVendedor} {objeto.vendedor} {objeto.listaPrecio} {objeto.saldo}\n")
                print("Archivo generado¡¡")


                 
        

    def main(self):


        

        menu=False

        while menu==False:

            print("-------MENU--------")
            print("a- Importar Datos")
            print("b- Clientes por Vendedor")
            print("c- Clientes por Lista de Precio")
            print("d- Clientes por Rango Saldo")
            print("e- Salir")
            print("--------------------")
            opcion=input().lower()

            if opcion=="a":
                self.importar_datos()

            elif opcion=="b":
                self.clientes_por_vendedor()

            elif opcion=="c":
                self.cliente_lista_precio()

            elif opcion=="d":
                self.cliente_rango_saldo()

            elif opcion=="e":
                menu=True

            else:
                print("Error de menu¡¡")


instanciaMain=ReportesMain()
instanciaMain.main()