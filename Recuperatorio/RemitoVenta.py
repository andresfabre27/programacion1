class RemitoVenta:

    def __init__(self,nombreCliente,numeroRemito,totalVenta=0):
        self.nombreCliente=nombreCliente
        self.numeroRemito=numeroRemito
        self.totalVenta=totalVenta
        self.detallesRemito=[]

    def agregar_detallesRemito(self,valor):
        self.detallesRemito.append(valor)