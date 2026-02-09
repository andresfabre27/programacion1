class Boxeador:
    def __init__(self,codigo,nombreCompleto,fuerza,agilidad,stamina,reflejos,tecnica,iq_boxeo):
        
        self.codigo=codigo
        self.nombreCompleto=nombreCompleto
        self.fuerza=fuerza
        self.agilidad=agilidad
        self.stemina=stamina
        self.reflejos=reflejos
        self.tecnica=tecnica
        self.iq_boxeo=iq_boxeo
        self.promedio=((fuerza+agilidad+stamina+reflejos+tecnica+iq_boxeo)/6)