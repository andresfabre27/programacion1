class DetalleOrdenCompra:
    def __init__(self,cantidad,producto):
        self.cantidad=cantidad
        self.producto=producto #objeto¡¡¡
        self.subtotal=self.cantidad*int(producto.precioCompra)