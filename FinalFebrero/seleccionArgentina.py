from Jugador import Jugador
import os    

direccion=os.path.join(os.path.dirname(__file__), 'seleccionArgentina.txt')

class seleccionArgentina:
    def __init__(self):
        self.jugadoresSeleccion={}
        self.indicadores=[["Distancia recorrida",0,0,0],
                          ["Precisión de pases (%)",0,0,0],
                          ["Duelos ganados",0,0,0],
                          ["Acciones decisivas",0,0,0],
                        ]
        
        self.evaluacionesFinales=[]


    def generar_diccionario(self):

        with open(direccion,"r",encoding="utf-8") as archivo:
            for linea in archivo:
                linea=linea.strip()
                temp=linea.split(";")
                instanciaJugador=Jugador(int(temp[0]),temp[1],int(temp[2]),temp[3])
                self.jugadoresSeleccion[int(temp[0])]=instanciaJugador
            print("Diccionario Creado!!")

    def asignar_escala_ponderacion(self,posicion,indicador):
        
        if posicion=="ARQ":
            if indicador=="Distancia recorrida":
                return 0.5
            elif indicador=="Precisión de pases (%)":
                return 0.29
            elif indicador=="Duelos ganados":
                return 0.35
            elif indicador=="Acciones decisivas":
                return 0.40
    
        elif posicion=="DEF":
            if indicador=="Distancia recorrida":
                return 0.15
            elif indicador=="Precisión de pases (%)":
                return 0.25
            elif indicador=="Duelos ganados":
                return 0.30
            elif indicador=="Acciones decisivas":
                return 0.30
        elif posicion=="MED":
            if indicador=="Distancia recorrida":
                return 0.25
            elif indicador=="Precisión de pases (%)":
                return 0.30
            elif indicador=="Duelos ganados":
                return 0.30
            elif indicador=="Acciones decisivas":
                return 0.15
        elif posicion=="DEL":
            if indicador=="Distancia recorrida":
                return 0.10
            elif indicador=="Precisión de pases (%)":
                return 0.15
            elif indicador=="Duelos ganados":
                return 0.30
            elif indicador=="Acciones decisivas":
                return 0.45
        




    def main(self):
        self.generar_diccionario()

        while True:
            while True:
                numerojugador=int(input("Ingrese el numero del jugador a evaluar: "))
                if numerojugador in self.jugadoresSeleccion:
                    print("Jugador encontrado!!")
                    objeto=self.jugadoresSeleccion[numerojugador]
                    break
                else:
                    print("Jugador no encontrado, intente nuevamente")

            print(f"Jugador: {objeto.nombreCompleto}")
            print("Ingrese los valores")
            contador=0
            suma=0
            for lista in self.indicadores:
                print(f"Indicador: {lista[0]}")
                valor=float(input("ingrese el valor: "))
                self.indicadores[contador][1]=valor
                self.indicadores[contador][2]=self.asignar_escala_ponderacion(objeto.puesto,lista[0])
                self.indicadores[contador][3]=valor*self.asignar_escala_ponderacion(objeto.puesto,lista[0])
                suma+=self.indicadores[contador][3]
                contador+=1
                

            print("indicador | valor asignado | ponderacion | resultado")
            for lista in self.indicadores:
                print(f"{lista[0]} | {lista[1]} | {lista[2]} | {lista[3]}")

            promedio=suma/4

            lista=[objeto.nombreCompleto,promedio]
            self.evaluacionesFinales.append(lista)

            opcion=input("¿Desea agregar otro alumno? S/N ").upper()

            if opcion=="S":
                pass
            elif opcion=="N":
                break

        print(self.evaluacionesFinales)

        mayorpromedio=0
        for lista in self.evaluacionesFinales:
            if lista[1]>mayorpromedio:
                mayorpromedio=lista[1]
        
        mejor_jugador=[]
        for lista in self.evaluacionesFinales:
            if lista[1]==mayorpromedio:
                mejor_jugador.append(lista[0])

        print(f"El/los mejores jugadores son: {mejor_jugador} con promedio {mayorpromedio}")




            

        





instanciaMain=seleccionArgentina() 
instanciaMain.main()