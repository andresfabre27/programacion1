from Boxeador import Boxeador
from ComparativaBoxeador import ComparativaBoxeador
import os

direccion=os.path.join(os.path.dirname(__file__), 'boxeadores_top.txt')


class EstadisticaMain:
    def __init__(self):
        self.diccionarioBoxeadores={}
        self.historialComparativa=[]

    def agregar_historialComparativa(self,valor):
        self.historialComparativa.append(valor)

    def definir_objetos(self):

        with open(direccion,"r") as archivo:
            next(archivo)
            for linea in archivo:
                temp=linea.split(";")
                instanciaBoxeador=Boxeador(int(temp[0].strip()),temp[1].strip(),int(temp[2].strip()),int(temp[3].strip()),int(temp[4].strip()),int(temp[5].strip()),int(temp[6].strip()),int(temp[7].strip()))
                self.diccionarioBoxeadores[int(temp[0].strip())]=instanciaBoxeador

        print("Objetos definidos!!")

    def mejor_boxeador_score(self):
        mayor=0
        mejores=[]
        for objeto in self.diccionarioBoxeadores.values():
            if objeto.promedio>mayor:
                mayor=objeto.promedio

        for objeto in self.diccionarioBoxeadores.values():
            if objeto.promedio>=mayor:
                mejores.append(objeto.nombreCompleto)
        print(f"El mejor promedio es: {mayor}")
        print(f"Los boxeadores con mejor promedio son: {mejores}")

    def comparar_boxeadores(self):

        while True:
            codigo1=int(input("Ingrese el codigo del primer boxeador a comparar: "))
            codigo2=int(input("Ingrese el codigo del segundo boxeador a comparar: "))
            if codigo1 != codigo2:
                break
            elif codigo1==codigo2:
                print("No puede validar el mismo boxeador, intente nuevamente")

        objeto1=self.diccionarioBoxeadores[codigo1]
        objeto2=self.diccionarioBoxeadores[codigo2]

        if objeto1.promedio==objeto2.promedio:
            ganador=None

        elif objeto1.promedio>objeto2.promedio:
            ganador=objeto1
        
        elif objeto1.promedio<objeto2.promedio:
            ganador=objeto2

        instanciaComparativaBoxeador=ComparativaBoxeador(objeto1,objeto2,ganador)
        self.agregar_historialComparativa(instanciaComparativaBoxeador)

        if ganador==None:
            print(" Los 2 boxeadores empatan!!")
            return

        print(f"El boxeador ganados es: {ganador.nombreCompleto} con promedio: {ganador.promedio}")

        
    def historico_comparativas(self):

        if len(self.historialComparativa)==0:
            print("No hay comparativas cargadas!!")
            return

        for objeto in self.historialComparativa:
            obj1=objeto.boxeadorUno
            obj2=objeto.boxeadorDos
            obj3=objeto.boxeadorGanador
            if obj3==None:
                print(f"Boxeador 1: {obj1.nombreCompleto} score: {obj1.promedio} VS Boxeador 2: {obj2.nombreCompleto} score: {obj2.promedio} Ganador= EMPATE!!")
            
            elif obj3!=None:
                print(f"Boxeador 1: {obj1.nombreCompleto} score: {obj1.promedio} VS Boxeador 2: {obj2.nombreCompleto} score: {obj2.promedio} Ganador= {obj3.nombreCompleto}")

    def exportar_historico_comparativas(self):

        if len(self.historialComparativa)==0:
            print("No hay comparativas cargadas!!")
            return

        direccion2=os.path.join(os.path.dirname(__file__), 'comparativa_boxeadores.txt')
        with open(direccion2,"w") as archivo:

            for objeto in self.historialComparativa:
                obj1=objeto.boxeadorUno
                obj2=objeto.boxeadorDos
                obj3=objeto.boxeadorGanador
                if obj3==None:
                    archivo.write(f"Boxeador 1: {obj1.nombreCompleto} score: {obj1.promedio} VS Boxeador 2: {obj2.nombreCompleto} score: {obj2.promedio} Ganador= EMPATE!!\n")
            
                elif obj3!=None:
                    archivo.write(f"Boxeador 1: {obj1.nombreCompleto} score: {obj1.promedio} VS Boxeador 2: {obj2.nombreCompleto} score: {obj2.promedio} Ganador= {obj3.nombreCompleto}\n")
            print("Archivo generado!!")




    def main(self):
        
        self.definir_objetos()

        menu=False
        while menu==False:
            print("a- Mejor Boxeador por score total ponderado")
            print("b- Comparar Boxeadores")
            print("c- Listar Histórico de Comparativa Boxeadores")
            print("d- Exportar Histórico Comparativa Boxeadores")
            print("e- Salir")
            opcion=input().lower()

            if opcion=="a":
                self.mejor_boxeador_score()

            elif opcion=="b":
                self.comparar_boxeadores()

            elif opcion=="c":
                self.historico_comparativas()

            elif opcion=="d":
                self.exportar_historico_comparativas()

            elif opcion=="e":
                menu=True

            else:
                print("Error de menu!! intente nuevamente")


instanciaMain=EstadisticaMain()
instanciaMain.main()