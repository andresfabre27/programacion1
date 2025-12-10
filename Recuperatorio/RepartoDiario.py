class RepartoDiario:
    def __init__(self,fecha,totalReparto=0):
        self.fecha=fecha
        self.remitosVenta=[]
        self.totalReparto=totalReparto

    def agregar_remitosVenta(self,valor):
        self.remitosVenta.append(valor)