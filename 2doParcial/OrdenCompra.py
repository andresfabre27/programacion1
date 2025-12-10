class OrdenCompra:
    def __init__(self,fecha,numero):
        self.fecha=fecha
        self.numero=numero
        self.total=0
        self.listaDetalles=[]

    def agregar_listaDetalles(self,valor):

        self.listaDetalles.append(valor)
        