class Cliente:

    def __init__(self, dni, nombre_completo, edad, carnets, descuento = 0, premium = False, gastado_premium = 0, total_gastado = 0, total_ahorrado = 0):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = int(edad)
        self.carnets = carnets
        self._descuento = 0
        self._premium = False
        self._gastado_premium = 0 #dinero gastado por el cliente que cuenta para el descuento premium
        self._total_gastado = 0 #dinero total gastado por el cliente
        self._total_ahorrado = 0 #dinero ahorrado por el cliente gracias al descuento por ser premium

    @classmethod
    def alta_Cliente(cls, dni, nombre_completo, edad, carnets, descuento = 0): #crea un cliente aceptando lista de carnets
        return cls(dni, nombre_completo, edad, carnets, descuento)

    def comprobar_premium(self): #comprueba si el cliente es premium (debe cumnplir haber gastado más de 500€) y actualiza sus datos
        if not self._premium and self._total_gastado >= 500:
            self._gastado_premium = self._total_gastado - 500
            self._premium = True

    def descuento_premium(self): #calcula el descuento por ser premium
        descuento_actual = 0
        if self._premium:
            descuento_actual = (self._gastado_premium // 100) * 15
            self._gastado_premium %= 100 #actualiza el saldo premium (puede quedar algo para el siguiente descuento)
            self._total_ahorrado += descuento_actual
        return descuento_actual