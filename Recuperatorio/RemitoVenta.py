class RemitoVenta:
    def __init__(self,nombreCliente,numeroRemito):
        self.nombreCliente=nombreCliente
        self.numeroRemito=numeroRemito
        self.totalVenta=0
        self.detallesRemito=[]

    def agregarDetallesRemito(self,valor):
        self.detallesRemito.append(valor)