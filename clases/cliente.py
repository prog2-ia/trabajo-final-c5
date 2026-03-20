class Cliente:

    def __init__(self, dni, nombre_completo, edad, carnets, descuento = 0, premium = False, gastado_premium = 0, total_gastado = 0, total_ahorrado = 0):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.carnets = carnets
        self._descuento = 0
        self._premium = False
        self._gastado_premium = 0
        self._total_gastado = 0
        self._total_ahorrado = 0

    @classmethod
    def alta_Cliente(cls, dni, nombre_completo, edad, carnets, descuento = 0):
        return cls(dni, nombre_completo, edad, carnets, descuento)

    def comprobar_premium(self):
        if not self._premium and self._total_gastado >= 500:
            self._gastado_premium = self._total_gastado - 500
            self._premium = True

    def descuento_premium(self):
        if self._premium:
            self._descuento += self._gastado_premium // 100 * 15
            self._gastado_premium %= 100
            return self._descuento