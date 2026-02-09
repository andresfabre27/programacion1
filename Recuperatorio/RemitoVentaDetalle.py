class RemitoVentaDetalle:
    def __init__(self,cantidad,articulo):
        self.cantidad=cantidad
        self.articulo=articulo #objeto
        self.subtotal=self.cantidad*articulo.precio