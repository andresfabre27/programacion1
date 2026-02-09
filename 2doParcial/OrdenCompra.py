class OrdenCompra:
    def __init__(self,fecha,):

        self.fecha=fecha
        self.numero=0
        self.total=0
        self.listaDetalles=[]

    def agregar_listaDetalles(self,valor):

        self.listaDetalles.append(valor)