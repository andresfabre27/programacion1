

golosinas=[[1, "KitKat", 20],
           [2, "Chicles", 50],
           [3, "Caramelos de Menta", 50],
           [4, "Huevo Kinder", 10],
           [5, "Chetoos", 10],
           [6, "Twix", 10],
           [7, "M&M S", 10],
           [8, "Papas Lays", 2],
           [9, "Milkybar", 10],
           [10, "Alfajor Tofi", 15],
           [11, "Lata Coca", 20],
           [12, "Chitos", 10]]

empleados={ 1100: "José Alonso",
            1200: "Federico Pacheco",
            1300: "Nelson Pereira",
            1400: "Osvaldo Tejada",
            1500: "Gastón Garcia"
            }

clavesTecnico=("admin","CCCDDD",2020)

golosinasPedidas=[["Código golosina", "Denominación Golosina", "Cantidad total pedida"]
                  
                  
                  ]

def imprimir_menu():

    print("--------------------")
    print("A-Pedir Golosina   ")
    print("B-Mostrar Golosina")
    print("C-Rellenar Golosina")
    print("D-Apagar Maquina")
    print("--------------------")

def buscar_golosina(golosinas,valor):

    for i in range(len(golosinas)):
        if golosinas[i][0] == valor:
            return i  # índice de la fila
    return -1 



def pedir_golosina(golosinas,empleados,golosinasPedidas):

    legajo=int(input("Ingrese su legajo: "))
    if legajo in empleados.keys():
        golosina=int(input("Ingrese el codigo de la golosina: "))
        if buscar_golosina(golosinas,golosina)!=-1:
            indice=buscar_golosina(golosinas,golosina)
            if golosinas[indice][2]>0:
                cantidad=int(input("Ingrese la cantidad que quiere sacar: "))
                if golosinas[indice][2]-cantidad>0:
                    golosinas[indice][2]-=cantidad
                    print("Hecho")
                    indice2=buscar_golosina(golosinasPedidas,golosina)
                    if indice2!=-1:
                        golosinasPedidas[indice2][2]+=cantidad
                    
                    else:
                        
                        temp=[golosinas[indice][0],golosinas[indice][1],cantidad]
                        golosinasPedidas.append(temp)


                else:
                    print("No quedan de esas golosinas")
         
            else:
                print("No quedan de esas golosinas")
        else:
            print("La golosina no existe")
    else:
        print("Usted no es un empleado de la empresa")

def mostrar_golosinas(golosinas):
    contador=0
    for linea in golosinas:
        print(f"Golosina: {golosinas[contador][1]} Cantidad: {golosinas[contador][2]}")
        contador+=1

def rellenar_golosina(clavesTecnico,golosinas):
    opcion1=input("Ingrese la primer contraseña: ")
    if opcion1==clavesTecnico[0]:
        opcion2=input("Ingrese la segunda contraseña: ")
        if opcion2==clavesTecnico[1]:
            opcion3=int(input("Ingrese la tercer contraseña: "))
            if opcion3==clavesTecnico[2]:
                codigo=int(input("Ingrese el codigo de la golosina: "))
                indice = buscar_golosina(golosinas, codigo)
                if indice!=-1:
                    while True:
                        cantidad=int(input("Ingrese la cantidad a recargar: "))
                        if cantidad>0:
                            break
                        else:
                            print("La cantidad debe ser mallor que cero")
                    golosinas[indice][2]+=cantidad
                    print("Hecho")
                     
                else:
                    print("No se encontro la golosina")
                    

            else:
                print("No tiene permiso para ejecutar la función de recarga")
        else:
            print("No tiene permiso para ejecutar la función de recarga")   
    else: 
        print("No tiene permiso para ejecutar la función de recarga")
        
def salir(golosinasPedidas):
    for c1,c2,c3 in golosinasPedidas:
        print(f"{c1} {c2} {c3}")


        


menu=False

while menu==False:
    imprimir_menu()
    opcion=input()

    if opcion=="A":
        pedir_golosina(golosinas,empleados,golosinasPedidas)

    if opcion=="B":
        mostrar_golosinas(golosinas)

    if opcion=="C":
        rellenar_golosina(clavesTecnico,golosinas)

    if opcion=="D":
        salir(golosinasPedidas)
        menu=True