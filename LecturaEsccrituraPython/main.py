import os

direccion=os.path.join(os.path.dirname(__file__), 'alumnos.txt')
direccion2=os.path.join(os.path.dirname(__file__), 'aprobados.txt')



def leer_alumnos():
    with open(direccion,"r") as archivo:
        for linea in archivo:
            temp=linea.split(";")
            print(f"Nombre: {temp[0].strip()} {temp[1].strip()}, legajo: {temp[2].strip()},promedio: {temp[3].strip()}")

def agregar_alumno(diccionario):
    
    while True:
        try:
            legajo=int(input("Ingrese el legajo: "))
            if 10000<=legajo<=99999:
                break
            else:
                print("Legajo incorrecto")
        except ValueError:
            print("El legajo solo puede ser un numero")
  

    if validar_existe_alumno(legajo,diccionario)==-1:
        return -1
    nombre=input("Ingrese el nombre: ")
    while not nombre:
        print("El nombre no puede ser vacio")
        nombre=input("Ingrese el nombre: ")
    apellido=input("Ingrese el apellido: ")
    while not apellido:
        print("El apellido no puede ser vacio")
        apellido=input("Ingrese el apellido: ") 
    while True:
        try:
            promedio=int(input("Ingrese el promedio: "))
            if 0<promedio<=10:
                break
            else:
                print("El promedio es un numero entre 0 y 10")
        except:
            print("El promedio debe ser un numero")
    with open(direccion,"a") as archivo:
        archivo.write(f"{nombre};{apellido};{legajo};{promedio}\n")
        print("Echo¡¡")

def validar_existe_alumno(legajo,diccionario):
    if legajo in diccionario.keys():
        print("El legajo ya existe")
        return -1
    else:
        return 1
    
def guardar_aprobados():
    with open(direccion, "r") as archivo, open(direccion2,"w") as archivo2:

        for linea in archivo:
            temp=linea.split(";")
            if int(temp[3])>7:
                archivo2.write(f"Nombre: {temp[0]} {temp[1]}, promedio: {temp[3]}")

    with open(direccion2, "r") as archivo:
        print(archivo.read())


diccionario={}

with open(direccion,"r") as archivo:
    
    for linea in archivo:
        temp=linea.split(";")
        diccionario[int(temp[2])]=temp[0]+" "+temp[1] 
        
    print(diccionario)

menu=False

while menu==False:
    
    print("--------------")
    print("A- Ver alumnos")
    print("B- Agregar alumno")
    print("C- Generar y mostrar archivo de aprobados")
    print("D- Salir\n")
    opcion=input()

    if opcion=="A":
        leer_alumnos()

    elif opcion=="B":
        agregar_alumno(diccionario)

    elif opcion=="C":
        guardar_aprobados()

    elif opcion=="D":
        menu=True

    else:
        print("Error de menu")