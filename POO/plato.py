class Plato:
    def __init__(self,nombreCompleto,precio,esBebida):
        self.nombreCompleto=nombreCompleto
        self.precio=precio
        self.esBebida=esBebida
        self.lista_de_ingredientes=[]

    def agregar_ingrediente(self,elemento):

        self.lista_de_ingredientes.append(elemento)


    
