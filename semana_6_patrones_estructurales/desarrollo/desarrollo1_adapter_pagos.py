"""
DESARROLLO 1: Adaptador de pagos (dolares a soles)
(EJERCICIO NUEVO - NO es el ejemplo del PDF)
"""


class PasarelaDolares:
    def pagar_usd(self, monto):
        return f"Pago: ${monto} USD"


class AdaptadorSoles:
    def __init__(self, pasarela):
        self.pasarela = pasarela
        self.tipo_cambio = 3.75
    
    def pagar_soles(self, monto):
        monto_usd = monto / self.tipo_cambio
        return f"Convertido: S/{monto} -> {self.pasarela.pagar_usd(monto_usd)}"


pasarela = PasarelaDolares()
adaptador = AdaptadorSoles(pasarela)
print(adaptador.pagar_soles(375))
