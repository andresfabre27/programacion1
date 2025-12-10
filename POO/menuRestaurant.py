from ingrediente import Ingrediente
from plato import Plato


class MenuRestaurant:

    def __init__(self):
        self.platosMenu=[]

    def agregar_plato(self,valor):
        self.platosMenu.append(valor)


    def main(self):
        
        while True:
            
            nombre=input("Ingrese el nombre del plato: ")
            while not nombre:
                print("No ingreso ningun dato")
                nombre=input("Ingrese el nombre del plato: ")
            
            while True:
                try:
                    precio=float(input("Ingrese el precio del plato: "))
                    if precio<=0:
                        print("El precio debe ser mayor que cero")
                    else:
                        break
                except ValueError:
                    print("El precio debe ser un numero")
            while True:
                esBebida=input("¿Es bebida? Si/No: ")
                if not esBebida:
                    print("Error, no ongreso ningun dato")
                elif esBebida!="Si" and esBebida!="No":
                    print("Error, solo se acepta Si/No")
                else:
                    break
            instaciaPlato=Plato(nombre,precio,esBebida)
            self.agregar_plato(instaciaPlato)
            
            if esBebida=="No":
                while True:

                    nombreIngrediente=input("Ingrese el nombre del ingrediente: ")
                    while not nombreIngrediente:
                        print("Error, no ingreso ningun dato")
                        nombreIngrediente=input("Ingrese el nombre del ingrediente: ")
                    while True:
                        try:
                            cantidad=int(input("Ingrese la cantidad: "))
                            break
                        except ValueError:
                            print("Error, solo puede ser un numero")
                    medida=input("Ingrese la unidad de medida: ")
                    while not medida:
                        print("Error, no ingreso ningun dato")
                        medida=input("Ingrese la unidad de medida: ")

                    instanciaIngrediente=Ingrediente(nombreIngrediente,cantidad,medida)
                    instaciaPlato.agregar_ingrediente(instanciaIngrediente)
                    
                    while True:
                        opcion2=input("¿Desea agregar otro ingrediente? Si/No: ")
                        if not opcion2:
                            print("No ingreso ningun dato")
                        elif opcion2!="Si" and opcion2!="No":
                            print("Error, solo se permite Si/No")
                        else:
                            break

                    if opcion2=="No":
                        break
            while True:
                opcion1=input("¿Desea agregar otro plato? Si/No:  ")
                if not opcion1:
                    print("No ingreso ningun dato")
                elif opcion1!="Si" and opcion1!="No":
                    print("Error, solo se acepta Si/No")
                else:
                    break

            if opcion1=="No":
                break
        
        print("-----MENU-----")
        for objeto in self.platosMenu:
            print(f"Nombre: {objeto.nombreCompleto}")
            print(f"Precio ${objeto.precio}")
            if objeto.esBebida=="No":
                print("Ingredientes: ")
                for objeto2 in objeto.lista_de_ingredientes:

                    print(f"Nombre: {objeto2.nombre}")
                    print(f"Cantidad: {objeto2.unidad_de_medida}{objeto2.cantidad}")
            print("---------------")





instanciamain=MenuRestaurant()
instanciamain.main()