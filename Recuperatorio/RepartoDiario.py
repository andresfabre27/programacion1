class RepartoDiario:
    def __init__(self,fecha):

        self.fecha=fecha
        self.totalReparto=0
        self.remitosVenta=[]

    def agregar_remitosVenta(self,valor):

        self.remitosVenta.append(valor)