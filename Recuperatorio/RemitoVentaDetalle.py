class RemitoVentaDetalle:
    def __init__(self,cantidad,articulo,subtotal):
        self.cantidad=cantidad
        self.articulo=articulo
        self.subtotal=subtotal

        self.codigo=articulo.codigo
        self.denominacion=articulo.denominacion
        self.precio=articulo.precio