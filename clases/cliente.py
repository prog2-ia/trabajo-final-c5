class Cliente:

    def __init__(self, dni: str, nombre_completo: str, edad: int, carnets: list, descuento: float = 0, premium: bool = False, gastado_premium: float = 0, total_gastado: float = 0, total_ahorrado: float = 0) -> None:
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = int(edad)
        self.carnets = carnets
        self._descuento = descuento
        self._premium = premium
        self._gastado_premium = gastado_premium #dinero gastado por el cliente que cuenta para el descuento premium
        self._total_gastado = total_gastado #dinero total gastado por el cliente
        self._total_ahorrado = total_ahorrado #dinero ahorrado por el cliente gracias al descuento por ser premium

    @property
    def total_gastado(self) -> float:
        return self._total_gastado

    @total_gastado.setter
    def total_gastado(self, valor: float) -> None:
        self._total_gastado = valor

    @property
    def gastado_premium(self) -> float:
        return self._gastado_premium

    @gastado_premium.setter
    def gastado_premium(self, valor: float) -> None:
        self._gastado_premium = valor

    @property
    def premium(self) -> bool:
        return self._premium

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

    def __iadd__(self, nuevo_carnet): #anadir carnets nuevos en caso de que haga falta
        self.carnets.append(nuevo_carnet)
        return self